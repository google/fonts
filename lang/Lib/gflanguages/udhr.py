from gflanguages import languages_public_pb2
import enum
import re


class Udhr:
    def __init__(
        self, key, iso639_3, iso15924, bcp47, direction, ohchr, stage, loc, name
    ):
        self.key = key
        self.iso639_3 = iso639_3
        self.iso15924 = iso15924
        self.bcp47 = bcp47
        self.direction = direction
        self.ohchr = ohchr
        self.stage = stage
        self.loc = loc
        self.name = name

        self.title = None
        self.preamble = None
        self.articles = []

    def Parse(self, translation_data):
        if translation_data is None or self.stage < 2:
            return

        if translation_data.find("./{*}title") is not None:
            self.title = translation_data.find("./{*}title").text

        preamble_data = translation_data.find("./{*}preamble")
        if preamble_data is not None:
            if preamble_data.find("./{*}title") is not None:
                self.preamble = {
                    "title": preamble_data.find("./{*}title").text,
                    "content": [
                        para.text for para in preamble_data.findall("./{*}para")
                    ],
                }

        articles_data = translation_data.findall("./{*}article")
        for article_data in articles_data:
            title_data = article_data.find("./{*}title")
            article = {
                "id": int(article_data.get("number")),
                "title": None if title_data is None else title_data.text,
                "content": [para.text for para in article_data.findall("./{*}para")],
            }
            self.articles.append(article)

    def LoadArticleOne(self, article_one):
        self.articles.append({"id": 0, "title": None, "content": [article_one]})

    def GetSampleTexts(self):
        extractor = SampleTextExtractor(self)
        return extractor.GetSampleTexts()


class SampleTextExtractor:
    class TextType(enum.Enum):
        GLYPHS = 1
        WORD = 2
        PHRASE = 3
        SENTENCE = 4
        PARAGRAPH = 5
        PASSAGE = 6

    def __init__(self, udhr):
        self._udhr = udhr
        self._glyphs = iter(self._GetGlyphs())
        self._words = iter(self._GetWords())
        self._paragraphs = iter(self._GetParagraphs())
        self._phrase_history = set()

        self._non_word_regex = re.compile(r"[^\w]+")
        self._space_regex = re.compile(r"\s+")
        self._non_space_regex = re.compile(r"[^\s]+")
        self._non_word_space_regex = re.compile(r"[^\w\s]+")
        self._any_regex = re.compile(r".")

    def _DisplayLength(self, s):
        """Returns length of given string. Omits combining characters.

        Some entire scripts will not be counted; in those cases, the raw length of
        the string is returned.
        """
        word_space_length = len(self._non_word_space_regex.sub("", s))
        space_length = len(self._non_space_regex.sub("", s))
        if word_space_length == space_length:
            return len(s)
        return word_space_length

    def _GetGlyphs(self):
        seen = set()
        for article in self._udhr.articles:
            for para in article["content"]:
                for ch in self._non_word_regex.sub("", para) or self._space_regex.sub(
                    "", para
                ):
                    ch = ch.lower()
                    if ch not in seen:
                        seen.add(ch)
                        yield ch

    def _GetWords(self):
        if self._space_regex.search(self._udhr.articles[0]["content"][0]) is not None:
            splitter = self._space_regex
        else:
            splitter = self._non_word_regex

        seen = set()
        for article in self._udhr.articles:
            for para in article["content"]:
                for s in splitter.split(para):
                    if s not in seen:
                        seen.add(s)
                        yield s

    def _GetParagraphs(self):
        if self._udhr.preamble is not None:
            for para in self._udhr.preamble["content"]:
                yield para
        for article in self._udhr.articles:
            for para in article["content"]:
                yield para

    def _ExtractGlyphs(self, min_chars, max_chars):
        s = ""
        for ch in self._glyphs:
            s += ch.upper()
            if len(s) >= min_chars:
                break
            if ch != ch.upper():
                s += ch
                if len(s) >= min_chars:
                    break
        return s

    def _ExtractWord(self, min_chars, max_chars):
        for iterator in [self._words, self._GetWords()]:
            for w in iterator:
                if w is None:
                    continue
                if min_chars <= self._DisplayLength(w) <= max_chars:
                    return w
        # Fallback to using multiple words for languages with very small words
        return self._ExtractPhrase(min_chars, max_chars)

    def _ExtractPhrase(self, min_chars, max_chars):
        for iterator in [self._paragraphs, self._GetParagraphs()]:
            for para in iterator:
                if para is None:
                    continue
                for regex in [self._any_regex, self._space_regex, self._non_word_regex]:
                    breaks = [-1]
                    for match in regex.finditer(para, min_chars):
                        breaks.append(match.start())
                        phrase = para[breaks[0] + 1 : breaks[len(breaks) - 1]]
                        p_size = self._DisplayLength(phrase)
                        while p_size > max_chars and len(breaks) > 1:
                            breaks.pop()
                            phrase = para[breaks[0] + 1 : breaks[len(breaks) - 1]]
                            p_size = self._DisplayLength(phrase)
                        if min_chars <= p_size and phrase not in self._phrase_history:
                            self._phrase_history.add(phrase)
                            return phrase
        return self._ExtractParagraph(min_chars, max_chars)

    def _ExtractSentence(self, min_chars, max_chars):
        # Sentence delimination may differ between scripts, so tokenizing on spaces
        # would be unreliable. Prefer to use _ExtractPhrase.
        return self._ExtractPhrase(min_chars, max_chars)

    def _ExtractParagraph(self, min_chars, max_chars):
        for iterator in [self._paragraphs, self._GetParagraphs()]:
            for para in iterator:
                if para is None:
                    continue
                if min_chars <= self._DisplayLength(para) <= max_chars:
                    return para
        # Paragraphs likely insufficient length; try combining into passages
        return self._ExtractPassage(min_chars, max_chars)

    def _ExtractPassage(self, min_chars, max_chars):
        p = []
        p_size = 0
        while p_size < min_chars:
            for iterator in [self._paragraphs, self._GetParagraphs()]:
                for para in iterator:
                    if para is None:
                        continue
                    p.append(para)
                    p_size = self._DisplayLength(" ".join(p))
                    if max_chars < p_size:
                        p.pop()
                    elif min_chars <= p_size:
                        return "\n".join(p)
        assert len(p) > 0, "Unable to extract passage: " + self._udhr.key
        if len(p) == 0:
            p.append([p for p in self._GetParagraphs()][0])
        return "\n".join(p)

    def _Get(self, text_type, **kwargs):
        if "char_count" in kwargs:
            min_chars = kwargs["char_count"]
            max_chars = kwargs["char_count"]
        else:
            min_chars = kwargs["min_chars"]
            max_chars = kwargs["max_chars"]
        if text_type == self.TextType.GLYPHS:
            return self._ExtractGlyphs(min_chars, max_chars)
        if text_type == self.TextType.WORD:
            return self._ExtractWord(min_chars, max_chars)
        if text_type == self.TextType.PHRASE:
            return self._ExtractPhrase(min_chars, max_chars)
        if text_type == self.TextType.SENTENCE:
            return self._ExtractSentence(min_chars, max_chars)
        if text_type == self.TextType.PARAGRAPH:
            return self._ExtractParagraph(min_chars, max_chars)
        if text_type == self.TextType.PASSAGE:
            return self._ExtractPassage(min_chars, max_chars)
        raise Exception("Unsupported text type: " + text_type)

    def GetSampleTexts(self):
        sample_text = languages_public_pb2.SampleTextProto()
        sample_text.masthead_full = self._Get(self.TextType.GLYPHS, char_count=4)
        sample_text.masthead_partial = self._Get(self.TextType.GLYPHS, char_count=2)
        sample_text.styles = self._Get(self.TextType.PHRASE, min_chars=40, max_chars=60)
        sample_text.tester = self._Get(self.TextType.PHRASE, min_chars=60, max_chars=90)
        sample_text.poster_sm = self._Get(
            self.TextType.PHRASE, min_chars=10, max_chars=17
        )
        sample_text.poster_md = self._Get(
            self.TextType.PHRASE, min_chars=6, max_chars=12
        )
        sample_text.poster_lg = self._Get(self.TextType.WORD, min_chars=3, max_chars=8)
        sample_text.specimen_48 = self._Get(
            self.TextType.SENTENCE, min_chars=50, max_chars=80
        )
        sample_text.specimen_36 = self._Get(
            self.TextType.PARAGRAPH, min_chars=100, max_chars=120
        )
        sample_text.specimen_32 = self._Get(
            self.TextType.PARAGRAPH, min_chars=140, max_chars=180
        )
        sample_text.specimen_21 = self._Get(
            self.TextType.PASSAGE, min_chars=300, max_chars=500
        )
        sample_text.specimen_16 = self._Get(
            self.TextType.PASSAGE, min_chars=550, max_chars=750
        )
        return sample_text
