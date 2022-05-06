from fontTools.ttLib import TTFont
from fontTools.misc.testTools import getXML, parseXML
from axisregistry import GFNameBuilder
import pytest
import os

CWD = os.path.dirname(__file__)
DATA_DIR = os.path.join(CWD, "data")

roboto_flex_fp = os.path.join(
    DATA_DIR,
    "RobotoFlex[GRAD,XOPQ,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,opsz,slnt,wdth,wght].ttf",
)
mavenpro_fp = os.path.join(DATA_DIR, "MavenPro-Regular.ttf")
opensans_roman_fp = os.path.join(DATA_DIR, "OpenSans[wdth,wght].ttf")
opensans_italic_fp = os.path.join(DATA_DIR, "OpenSans-Italic[wdth,wght].ttf")
opensans_cond_roman_fp = os.path.join(DATA_DIR, "OpenSansCondensed[wght].ttf")
opensans_cond_italic_fp = os.path.join(DATA_DIR, "OpenSansCondensed-Italic[wght].ttf")


@pytest.fixture
def static_font():
    return TTFont(mavenpro_fp)


def _test_names(ttFont, expected):
    name_table = ttFont["name"]
    for k, v in expected.items():
        record = name_table.getName(*k)
        if not record:
            assert record == v, f"{k} record is incorrect, expected {v} got {record}"
        else:
            record_string = record.toUnicode()
            assert (
                record_string == v
            ), f"{k} record is incorrect, expected {v} got {record}"


@pytest.mark.parametrize(
    "family_name, style_name, expected",
    [
        # Maven Pro Regular
        (
            "Maven Pro",
            "Regular",
            {
                (1, 3, 1, 0x409): "Maven Pro",
                (2, 3, 1, 0x409): "Regular",
                (3, 3, 1, 0x409): "2.003;NONE;MavenPro-Regular",
                (4, 3, 1, 0x409): "Maven Pro Regular",
                (6, 3, 1, 0x409): "MavenPro-Regular",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
            },
        ),
        # Maven Pro Italic
        (
            "Maven Pro",
            "Italic",
            {
                (1, 3, 1, 0x409): "Maven Pro",
                (2, 3, 1, 0x409): "Italic",
                (3, 3, 1, 0x409): "2.003;NONE;MavenPro-Italic",
                (4, 3, 1, 0x409): "Maven Pro Italic",
                (6, 3, 1, 0x409): "MavenPro-Italic",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
            },
        ),
        # Maven Pro Bold
        (
            "Maven Pro",
            "Bold",
            {
                (1, 3, 1, 0x409): "Maven Pro",
                (2, 3, 1, 0x409): "Bold",
                (3, 3, 1, 0x409): "2.003;NONE;MavenPro-Bold",
                (4, 3, 1, 0x409): "Maven Pro Bold",
                (6, 3, 1, 0x409): "MavenPro-Bold",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
            },
        ),
        # Maven Pro Bold Italic
        (
            "Maven Pro",
            "Bold Italic",
            {
                (1, 3, 1, 0x409): "Maven Pro",
                (2, 3, 1, 0x409): "Bold Italic",
                (3, 3, 1, 0x409): "2.003;NONE;MavenPro-BoldItalic",
                (4, 3, 1, 0x409): "Maven Pro Bold Italic",
                (6, 3, 1, 0x409): "MavenPro-BoldItalic",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
            },
        ),
        # Maven Pro Black
        (
            "Maven Pro",
            "Black",
            {
                (1, 3, 1, 0x409): "Maven Pro Black",
                (2, 3, 1, 0x409): "Regular",
                (3, 3, 1, 0x409): "2.003;NONE;MavenPro-Black",
                (4, 3, 1, 0x409): "Maven Pro Black",
                (6, 3, 1, 0x409): "MavenPro-Black",
                (16, 3, 1, 0x409): "Maven Pro",
                (17, 3, 1, 0x409): "Black",
            },
        ),
        # Maven Pro Black Italic
        (
            "Maven Pro",
            "Black Italic",
            {
                (1, 3, 1, 0x409): "Maven Pro Black",
                (2, 3, 1, 0x409): "Italic",
                (3, 3, 1, 0x409): "2.003;NONE;MavenPro-BlackItalic",
                (4, 3, 1, 0x409): "Maven Pro Black Italic",
                (6, 3, 1, 0x409): "MavenPro-BlackItalic",
                (16, 3, 1, 0x409): "Maven Pro",
                (17, 3, 1, 0x409): "Black Italic",
            },
        ),
        # Maven Pro ExtraLight Italic
        (
            "Maven Pro",
            "ExtraLight Italic",
            {
                (1, 3, 1, 0x409): "Maven Pro ExtraLight",
                (2, 3, 1, 0x409): "Italic",
                (3, 3, 1, 0x409): "2.003;NONE;MavenPro-ExtraLightItalic",
                (4, 3, 1, 0x409): "Maven Pro ExtraLight Italic",
                (6, 3, 1, 0x409): "MavenPro-ExtraLightItalic",
                (16, 3, 1, 0x409): "Maven Pro",
                (17, 3, 1, 0x409): "ExtraLight Italic",
            },
        ),
        # check non-weight styles get appended to family name
        # Maven Pro UltraExpanded Regular
        (
            "Maven Pro",
            "UltraExpanded Regular",
            {
                (1, 3, 1, 0x409): "Maven Pro UltraExpanded",
                (2, 3, 1, 0x409): "Regular",
                (3, 3, 1, 0x409): "2.003;NONE;MavenProUltraExpanded-Regular",
                (4, 3, 1, 0x409): "Maven Pro UltraExpanded Regular",
                (6, 3, 1, 0x409): "MavenProUltraExpanded-Regular",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
            },
        ),
        # Maven Pro Condensed ExtraLight Italic
        (
            "Maven Pro",
            "Condensed ExtraLight Italic",
            {
                (1, 3, 1, 0x409): "Maven Pro Condensed ExtraLight",
                (2, 3, 1, 0x409): "Italic",
                (3, 3, 1, 0x409): "2.003;NONE;MavenProCondensed-ExtraLightItalic",
                (4, 3, 1, 0x409): "Maven Pro Condensed ExtraLight Italic",
                (6, 3, 1, 0x409): "MavenProCondensed-ExtraLightItalic",
                (16, 3, 1, 0x409): "Maven Pro Condensed",
                (17, 3, 1, 0x409): "ExtraLight Italic",
            },
        ),
    ],
)
def test_static_name_table(static_font, family_name, style_name, expected):
    builder = GFNameBuilder(static_font)
    builder.build_name_table(family_name, style_name)
    _test_names(static_font, expected)


@pytest.mark.parametrize(
    "font_fp, dflt_coords, expected",
    [
        # Condensed variants
        (
            opensans_cond_roman_fp,
            {},
            [
                ("Thin", {"wght": 100.0}),
                ("ExtraLight", {"wght": 200.0}),
                ("Light", {"wght": 300.0}),
                ("Regular", {"wght": 400.0}),
                ("Medium", {"wght": 500.0}),
                ("SemiBold", {"wght": 600.0}),
                ("Bold", {"wght": 700.0}),
                ("ExtraBold", {"wght": 800.0}),
            ],
        ),
        (
            opensans_cond_italic_fp,
            {},
            [
                ("Thin Italic", {"wght": 100.0}),
                ("ExtraLight Italic", {"wght": 200.0}),
                ("Light Italic", {"wght": 300.0}),
                ("Italic", {"wght": 400.0}),
                ("Medium Italic", {"wght": 500.0}),
                ("SemiBold Italic", {"wght": 600.0}),
                ("Bold Italic", {"wght": 700.0}),
                ("ExtraBold Italic", {"wght": 800.0}),
            ],
        ),
        # Multi axis + roman & ital with dflt coords
        (
            roboto_flex_fp,
            {},
            [
                ("Thin", {"wght": 100.0}),
                ("ExtraLight", {"wght": 200.0}),
                ("Light", {"wght": 300.0}),
                ("Regular", {"wght": 400.0}),
                ("Medium", {"wght": 500.0}),
                ("SemiBold", {"wght": 600.0}),
                ("Bold", {"wght": 700.0}),
                ("ExtraBold", {"wght": 800.0}),
                ("Black", {"wght": 900.0}),
                ("Thin Italic", {"wght": 100.0, "slnt": -10}),
                ("ExtraLight Italic", {"wght": 200.0, "slnt": -10}),
                ("Light Italic", {"wght": 300.0, "slnt": -10}),
                ("Italic", {"wght": 400.0, "slnt": -10}),
                ("Medium Italic", {"wght": 500.0, "slnt": -10}),
                ("SemiBold Italic", {"wght": 600.0, "slnt": -10}),
                ("Bold Italic", {"wght": 700.0, "slnt": -10}),
                ("ExtraBold Italic", {"wght": 800.0, "slnt": -10}),
                ("Black Italic", {"wght": 900.0, "slnt": -10}),
            ],
        ),
        # multi axis with METADATA.pb registry_default_overrides
        # https://github.com/google/fonts/blob/main/ofl/robotoflex/METADATA.pb
        (
            roboto_flex_fp,
            {
                "XOPQ": 96.0,
                "XTRA": 468.0,
                "YOPQ": 79.0,
                "YTDE": -203.0,
                "YTFI": 738.0,
                "YTLC": 514.0,
                "YTUC": 712.0,
            },
            [
                ("Thin", {"wght": 100.0}),
                ("ExtraLight", {"wght": 200.0}),
                ("Light", {"wght": 300.0}),
                ("Regular", {"wght": 400.0}),
                ("Medium", {"wght": 500.0}),
                ("SemiBold", {"wght": 600.0}),
                ("Bold", {"wght": 700.0}),
                ("ExtraBold", {"wght": 800.0}),
                ("Black", {"wght": 900.0}),
                ("Thin Italic", {"wght": 100.0, "slnt": -10}),
                ("ExtraLight Italic", {"wght": 200.0, "slnt": -10}),
                ("Light Italic", {"wght": 300.0, "slnt": -10}),
                ("Italic", {"wght": 400.0, "slnt": -10}),
                ("Medium Italic", {"wght": 500.0, "slnt": -10}),
                ("SemiBold Italic", {"wght": 600.0, "slnt": -10}),
                ("Bold Italic", {"wght": 700.0, "slnt": -10}),
                ("ExtraBold Italic", {"wght": 800.0, "slnt": -10}),
                ("Black Italic", {"wght": 900.0, "slnt": -10}),
            ],
        ),
    ],
)
def test_fvar_instances(font_fp, dflt_coords, expected):
    font = TTFont(font_fp)
    builder = GFNameBuilder(font)
    builder.build_fvar_instances(dflt_coords)
    fvar = font["fvar"]
    wght_axis = next((a for a in fvar.axes if a.axisTag == "wght"), None)
    wght_min = wght_axis.minValue
    wght_max = wght_axis.maxValue
    instances = fvar.instances
    if not dflt_coords:
        dflt_coords = {k: v["value"] for k, v in builder._fvar_dflts().items()}

    assert len(instances) == len(expected)
    for inst, (expected_name, coords) in zip(instances, expected):
        inst_name = font["name"].getName(inst.subfamilyNameID, 3, 1, 0x409).toUnicode()
        assert inst_name == expected_name
        for tag, val in coords.items():
            dflt_coords[tag] = val
        assert inst.coordinates == dflt_coords


def dump(table, ttFont=None):
    return "\n".join(getXML(table.toXML, ttFont))


@pytest.mark.parametrize(
    "fp, sibling_fps",
    [
        (roboto_flex_fp, []),
        (
            opensans_roman_fp,
            [opensans_italic_fp, opensans_cond_roman_fp, opensans_cond_italic_fp],
        ),
        (
            opensans_italic_fp,
            [opensans_roman_fp, opensans_cond_roman_fp, opensans_cond_italic_fp],
        ),
        (
            opensans_cond_roman_fp,
            [opensans_roman_fp, opensans_italic_fp, opensans_cond_italic_fp],
        ),
        (
            opensans_cond_italic_fp,
            [opensans_roman_fp, opensans_italic_fp, opensans_cond_roman_fp],
        ),
    ],
)
def test_stat(fp, sibling_fps):
    font = TTFont(fp)
    siblings = [TTFont(f) for f in sibling_fps]
    builder = GFNameBuilder(font)
    builder.build_stat(siblings)
    stat_fp = fp.replace(".ttf", "_STAT.ttx")

### output good files
#    with open(stat_fp, "w") as doc:
#        got = dump(font["STAT"], font)
#        doc.write(got)
#
    with open(stat_fp) as doc:
        expected = doc.read()
        got = dump(font["STAT"], font)
        assert got == expected
