import re
import random

from gfmetadata import languages_public_pb2
from google.protobuf.json_format import ParseDict
from google.protobuf.text_format import MessageToString

text = "𖺯 𖻎𖻊𖻄𖻄𖻊𖻊 𖻏𖺾𖻌𖺾𖺿 𖺼𖺾́𖻀𖻂𖻀𖺻 𖻀𖺻𖻌𖺽𖻂 𖺼𖺾́𖻀𖻂𖻀𖺻 𖻂𖻇𖻇𖺾𖻌 𖻐𖺾𖻓𖻂𖻍𖻂𖻂. 𖺰𖺾𖺾𖻌 𖺼𖺻́𖻌𖻂𖻂 𖺾𖻀𖺾𖻀𖻂𖻇𖺾𖺾 𖻄𖻂𖻓𖺾𖻍𖺾 𖺻𖻀𖻂𖻅 𖻀𖺻 𖻄𖻂𖺽𖻂𖻓𖺾𖻓𖻂. 𖺵𖻊𖻌𖺾 𖻇𖻂𖻀𖻑 𖻇𖻂 𖻁𖻂𖻓𖺾𖻀𖻂 𖺼𖺻𖻀𖺻𖻌𖺻𖺻𖻀𖻊 𖻂𖻇𖻇𖺾𖻌 𖻇𖻊𖻀𖻂𖻇𖻊𖻇𖻉 𖺽𖻂𖻍𖻊."

sentences = re.split(r"(?<=[。\.])\s+", text)
sentences = [s for s in sentences if s.strip()]

words = re.findall(r"\S+", text.replace(".", ""))
glyphs = set(re.findall(r"\S", text))


def random_phrase(inputs, min_len, max_len, separator=" "):
    phrase = ""
    satisfied = False
    repetitions = 1
    while not satisfied:
        sentence_bag = list(inputs) * repetitions
        remaining = max_len
        while remaining > 0 and len(sentence_bag) > 0:
            new_sentence = random.choice(sentence_bag)
            sentence_bag.remove(new_sentence)
            phrase += new_sentence + separator
            remaining -= len(new_sentence) + len(separator)
            if len(phrase) >= min_len:
                satisfied = True
                break
        if not satisfied:
            print("Trying again with a new bag of sentences")
            repetitions += 1
    return phrase


sample_text = {
    "masthead_full": "".join(random.choices(list(glyphs), k=4)),
    "masthead_partial": "".join(random.choices(list(glyphs), k=2)),
    "styles": random_phrase(sentences, 40, 60, ". "),
    "tester": random_phrase(sentences, 60, 90, ". "),
    "poster_sm": random_phrase(words, 10, 17, " "),
    "poster_md": random_phrase(words, 6, 12, " "),
    "poster_lg": random_phrase(words, 3, 8, " "),
    "specimen_48": random_phrase(sentences, 50, 80, ". "),
    "specimen_36": random_phrase(sentences, 100, 120, ". "),
    "specimen_32": random_phrase(sentences, 140, 180, ". "),
    "specimen_21": random_phrase(sentences, 300, 500, ". "),
    "specimen_16": random_phrase(sentences, 550, 750, ". "),
}
# print(words)
message = ParseDict(
    sample_text,
    languages_public_pb2.SampleTextProto(),
)
print(MessageToString(message, as_utf8=True))
