from collections import Counter
import unicodedata
from google.protobuf import text_format
from gflanguages import languages_public_pb2

ATTRIBUTES = "base auxiliary marks punctuation index".split(" ")


def main(args=None):
    for path in args:
        with open(path, encoding="utf-8") as fp:
            language = text_format.Parse(
                fp.read(), languages_public_pb2.LanguageProto()
            )
        changed = False
        exemplar_values = {}
        bases = language.exemplar_chars.base.split(" ")
        marks = language.exemplar_chars.marks.split(" ")
        if not len(bases) or bases == [""]:
            continue
        new_marks = []
        new_bases = []
        for chars in marks:
            if not chars:
                continue
            if chars[0] != "\u25CC":
                chars = "\u25CC" + chars
            if chars not in new_marks:
                new_marks.append(chars)

        for chars in bases:
            if not chars:
                continue
            if chars[0] == "\u25CC":
                chars = chars[1:]
            cat = unicodedata.category(chars[0])
            if cat in ["Mn", "Mc"]:
                if chars[0] != "\u25CC":
                    chars = "\u25CC" + chars
                if chars not in new_marks:
                    new_marks.append(chars)
            else:
                new_bases.append(chars)

        language.exemplar_chars.base = " ".join(new_bases)
        language.exemplar_chars.marks = " ".join(new_marks)

        with open(path, "w", encoding="utf-8") as fp:
            fp.write(text_format.MessageToString(language, as_utf8=True))
            fp.close()


if __name__ == "__main__":
    import sys

    main(args=sys.argv[1:])
