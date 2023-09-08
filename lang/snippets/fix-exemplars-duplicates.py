from collections import Counter
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
        if not hasattr(language, "exemplar_chars"):
            exit()
        for attr in ATTRIBUTES:
            if hasattr(language.exemplar_chars, attr):
                values = getattr(language.exemplar_chars, attr).split(" ")
                value_set = set()
                clean_values = []
                for value in values:
                    if value in value_set:
                        continue
                    else:
                        value_set.add(value)
                        clean_values.append(value)

                if clean_values != values:
                    if {len(set(values))} != {len(set(clean_values))}:
                        print("before: "+ " ".join(values))
                        print("after: "+ " ".join(clean_values))
                        sys.exit("Failed fixing exemplar.")
                    setattr(language.exemplar_chars, attr, " ".join(clean_values))
                    changed = True
                    exemplar_values[attr] = {
                        "before": values,
                        "after": clean_values
                    }

        if changed:
            for exemplar, values in exemplar_values.items():
                before = values["before"]
                after = values["after"]
                counter = Counter(before)
                duplicates = [(g, c - 1) for g, c in counter.most_common() if c > 1]
            print(
                f"Changed {path} {exemplar} exemplar:\n"
                f"- from {len(before)} ({len(set(before))} as set) "
                f"to {len(after)} elements\n"
                f"- removing {len(before) - len(after)} duplicate(s):\n"
                f"  {duplicates}\n"
            )
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(text_format.MessageToString(language, as_utf8=True))
                fp.close()


if __name__ == "__main__":
    import sys

    main(args=sys.argv[1:])
