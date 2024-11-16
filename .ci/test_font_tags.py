import json
from urllib.request import urlopen
import sys

prod_data = json.loads(
    urlopen("https://fonts.google.com/metadata/fonts").read().decode("utf-8")
)
prod_families = set(f["family"] for f in prod_data["familyMetadataList"])

csv_data = (
    urlopen("https://raw.githubusercontent.com/google/fonts/main/tags/all/families.csv")
    .read()
    .decode("utf-8")
)
csv_families = set(
    line.split(",")[0]
    for line in csv_data.split("\n")
    if line
    if line.split(",")[0] != "Family"
)

families_missing_tags = sorted(prod_families - csv_families)
families_missing_tags = [f for f in families_missing_tags if not f.endswith("SC")]

if families_missing_tags:
    missing_list = "\n".join(families_missing_tags)
    raise ValueError(
        f"The following {len(families_missing_tags)} families are missing tags:\n\n"
        f"{missing_list}\n\n"
        "Please add tags for these families using the following webapp: "
        "https://google.github.io/fonts/tags.html"
    )

sys.exit(0)
