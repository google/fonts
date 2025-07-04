import pytest
import json
from urllib.request import urlopen
import csv
import os

@pytest.fixture
def family_metadata():
    data = json.loads(
        urlopen("https://fonts.google.com/metadata/fonts").read().decode("utf-8")
    )
    return data["familyMetadataList"]


@pytest.fixture
def family_tags():
    fp = os.path.join(os.path.dirname(__file__), "..", "tags", "all", "families.csv")
    reader = csv.reader(open(fp, "r", encoding="utf-8"))
    res = []
    for row in reader:
        res.append([row[0], row[1], float(row[2])])
    return res


@pytest.fixture
def tags_metadata():
    data = (
        urlopen(
            "https://raw.githubusercontent.com/google/fonts/main/tags/tags_metadata.csv"
        )
        .read()
        .decode("utf-8")
    )
    reader = csv.reader(data.splitlines())
    res = []
    for category, _, _ in reader:
        res.append(category)
    return res


def test_families_missing_tags(family_tags, family_metadata):
    tagged_families = set(f[0] for f in family_tags)
    families_in_gf = set(f["family"] for f in family_metadata)
    families_missing_tags = sorted(families_in_gf - tagged_families)
    missing_list = "\n".join(families_missing_tags)

    assert len(families_missing_tags) == 0, (
        f"The following {len(families_missing_tags)} families are missing tags:\n\n"
        f"{missing_list}\n\n"
        "Please add tags for these families using the following webapp: "
        "https://google.github.io/fonts/tags.html"
    )


def test_categories_exist(family_tags, tags_metadata):
    """Every tag category in the families.csv file must also exist in the
    tags_metadata.csv file
    """
    meta_categories = set(tags_metadata)
    families_categories = set(cat for _, cat, _ in family_tags)
    missing = families_categories - meta_categories
    assert not missing, f"Missing categories: {missing}"


def test_no_duplicate_families(family_tags):
    seen = set()
    dups = []
    for family, cat, _ in family_tags:
        key = (family, cat)
        if key in seen:
            dups.append(",".join(key))
        seen.add(key)
    assert not dups, f"Duplicate tags found: {dups}"


def test_tag_vals_in_range(family_tags):
    out_of_range = []
    for family, cat, val in family_tags:
        if val <= 0 or val > 100:
            out_of_range.append((family, cat, val))
    assert not out_of_range, f"Values out of range 1-100: {out_of_range}"
