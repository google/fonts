from collections import defaultdict
import pytest
import ast
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
def tag_rules():
    fp = os.path.join(os.path.dirname(__file__), "..", "tagger2", "tag_rules.csv")
    reader = csv.reader(open(fp, "r", encoding="utf-8"))
    rules = [row for row in reader if row and not row[0].startswith("#")]
    return rules


@pytest.fixture
def tags_metadata():
    data = (
        urlopen(
            "https://raw.githubusercontent.com/google/fonts/main/tags/tags_metadata.csv"
        )
        .read()
        .decode("utf-8")
    )
    return data.splitlines()


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

def create_context(family, family_tags):
    """Evaluate a rule against a family name."""
    tag = defaultdict(lambda: float("nan"))
    for f, c, v in family_tags:
        if f == family:
            tag[c] = v
    font = {}
    font["OS/2"] = {"fsSelection": 0}  # Dummy value for now
    return {"tag": tag, "font": font, "family": family}

def test_rules_are_ok(tag_rules):
    """Check that the rules in tag_rules.csv are valid for the families.csv file."""
    for rule, severity, message in tag_rules:
        if severity not in ["WARN", "INFO", "FAIL"]:
            raise ValueError(f"Invalid severity '{severity}' in rule: {rule}")
        # Each rule should be a valid snippet of Python code
        try:
            ast.parse(rule)
        except SyntaxError as e:
            raise ValueError(f"Invalid rule syntax in rule '{rule}': {e}")

def test_rules(family_tags, tag_rules):
    """Check that the families are valid according to the rules."""
    tagged_families = set(f[0] for f in family_tags)
    problems = []
    for family in sorted(tagged_families):
        context = create_context(family, family_tags)
        for rule, severity, message in tag_rules:
            try:
                ok = not eval(rule, context)
            except Exception as e:
                raise ValueError(f"Error evaluating rule '{rule}' for family '{family}': {e}")
            if not ok and (severity == "FAIL" or severity == "WARN"):
                problems.append(
                    f"{family}: {message} ({severity})"
                )
    assert not problems, "\n".join(problems)
