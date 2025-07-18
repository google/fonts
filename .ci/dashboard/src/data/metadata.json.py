import json
import os
from glob import glob
from pathlib import Path
from gftools.util.google_fonts import Metadata, GetExemplarFont
from fontTools.ttLib import TTFont
from google.protobuf.json_format import MessageToDict
from gftools.push.items import parse_html

repo_path = os.environ["GF_REPO_PATH"]
metadata = {}

for directory in list(glob(os.path.join(repo_path, "ofl", "*"))) + list(glob(os.path.join(repo_path, "apache", "*"))):
    if not os.path.isdir(directory):
        continue

    try:
        md = Metadata(directory)
    except Exception as e:
        continue

    fp = Path(directory)

    this_md = metadata[fp.stem] = MessageToDict(md)
    # Also load font version, description, article
    try:
        exemplar = GetExemplarFont(md)
        font = TTFont(os.path.join(directory, exemplar.filename))
        this_md["version"] = font["name"].getName(5, 3, 1, 0x409).toUnicode()
    except Exception as e:
        this_md["version"] = "Error loading version: " + str(e)
    article_fp = fp / "article" / "ARTICLE.en_us.html"
    if article_fp.exists():
        this_md["article"] = parse_html(open(article_fp, encoding="utf-8").read())
    else:
        this_md["article"] = None

    description_fp = fp / "DESCRIPTION.en_us.html"
    if description_fp.exists():
        this_md["description"] = parse_html(
            open(description_fp, encoding="utf8").read()
        )
    else:
        this_md["description"] = None
    this_md["license"] = this_md["license"].lower()

print(json.dumps(metadata, indent=2, ensure_ascii=False))
