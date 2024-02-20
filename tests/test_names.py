from fontTools.ttLib import TTFont
from fontTools.misc.testTools import getXML
from axisregistry import (
    build_name_table,
    build_filename,
    build_fvar_instances,
    build_stat,
    build_variations_ps_name,
    _fvar_dflts,
    _fvar_instance_collisions,
)
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
wonky_fp = os.path.join(DATA_DIR, "Wonky[wdth,wght].ttf")
playfair_fp = os.path.join(DATA_DIR, "Playfair[opsz,wdth,wght].ttf")
wavefont_fp = os.path.join(DATA_DIR, "Wavefont[ROND,YALN,wght].ttf")


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
    "fp, family_name, style_name, siblings, expected",
    [
        # Maven Pro Regular
        (
            mavenpro_fp,
            "Maven Pro",
            "Regular",
            [],
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
            mavenpro_fp,
            "Maven Pro",
            "Italic",
            [],
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
            mavenpro_fp,
            "Maven Pro",
            "Bold",
            [],
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
            mavenpro_fp,
            "Maven Pro",
            "Bold Italic",
            [],
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
            mavenpro_fp,
            "Maven Pro",
            "Black",
            [],
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
            mavenpro_fp,
            "Maven Pro",
            "Black Italic",
            [],
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
            mavenpro_fp,
            "Maven Pro",
            "ExtraLight Italic",
            [],
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
            mavenpro_fp,
            "Maven Pro",
            "UltraExpanded Regular",
            [],
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
            mavenpro_fp,
            "Maven Pro",
            "Condensed ExtraLight Italic",
            [],
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
        ## VFs
        # Open Sans Roman
        (
            opensans_roman_fp,
            "Open Sans",
            None,
            [opensans_italic_fp, opensans_cond_roman_fp, opensans_cond_italic_fp],
            {
                (1, 3, 1, 0x409): "Open Sans",
                (2, 3, 1, 0x409): "Regular",
                (3, 3, 1, 0x409): "3.000;GOOG;OpenSans-Regular",
                (4, 3, 1, 0x409): "Open Sans Regular",
                (6, 3, 1, 0x409): "OpenSans-Regular",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
                (25, 3, 1, 0x409): "OpenSans",
            },
        ),
        # Open Sans Italic
        (
            opensans_italic_fp,
            "Open Sans",
            None,
            [opensans_roman_fp, opensans_cond_roman_fp, opensans_cond_italic_fp],
            {
                (1, 3, 1, 0x409): "Open Sans",
                (2, 3, 1, 0x409): "Italic",
                (3, 3, 1, 0x409): "3.000;GOOG;OpenSans-Italic",
                (4, 3, 1, 0x409): "Open Sans Italic",
                (6, 3, 1, 0x409): "OpenSans-Italic",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
                (25, 3, 1, 0x409): "OpenSansItalic",
            },
        ),
        # Open Sans Cond Roman
        (
            opensans_cond_roman_fp,
            "Open Sans Condensed",
            None,
            [opensans_roman_fp, opensans_italic_fp, opensans_cond_italic_fp],
            {
                (1, 3, 1, 0x409): "Open Sans Condensed",
                (2, 3, 1, 0x409): "Regular",
                (3, 3, 1, 0x409): "3.000;GOOG;OpenSansCondensed-Regular",
                (4, 3, 1, 0x409): "Open Sans Condensed Regular",
                (6, 3, 1, 0x409): "OpenSansCondensed-Regular",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
                (25, 3, 1, 0x409): "OpenSansCondensed",
            },
        ),
        # Open Sans Cond Italic
        (
            opensans_cond_italic_fp,
            "Open Sans Condensed",
            None,
            [opensans_roman_fp, opensans_italic_fp, opensans_cond_roman_fp],
            {
                (1, 3, 1, 0x409): "Open Sans Condensed",
                (2, 3, 1, 0x409): "Italic",
                (3, 3, 1, 0x409): "3.000;GOOG;OpenSansCondensed-Italic",
                (4, 3, 1, 0x409): "Open Sans Condensed Italic",
                (6, 3, 1, 0x409): "OpenSansCondensed-Italic",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
                (25, 3, 1, 0x409): "OpenSansCondensedItalic",
            },
        ),
        # Bad names
        (
            mavenpro_fp,
            "Maven Pro",
            "Fat",  # this should get appended to the family name
            [],
            {
                (1, 3, 1, 0x409): "Maven Pro Fat",
                (2, 3, 1, 0x409): "Regular",
                (3, 3, 1, 0x409): "2.003;NONE;MavenProFat-Regular",
                (4, 3, 1, 0x409): "Maven Pro Fat Regular",
                (6, 3, 1, 0x409): "MavenProFat-Regular",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
            },
        ),
        (
            wonky_fp,
            "Wonky",  # name exists in axis reg!
            None,
            [],
            {
                (1, 3, 1, 0x409): "Wonky",
                (2, 3, 1, 0x409): "Regular",
                (3, 3, 1, 0x409): "3.000;GOOG;Wonky-Regular",
                (4, 3, 1, 0x409): "Wonky Regular",
                (6, 3, 1, 0x409): "Wonky-Regular",
                (16, 3, 1, 0x409): None,
                (17, 3, 1, 0x409): None,
            },
        ),
        # Test opsz particle is kept.
        # Fixes https://github.com/googlefonts/axisregistry/issues/130
        (
            playfair_fp,
            "Playfair",
            None,
            [],
            {
                (1, 3, 1, 0x409): "Playfair SemiExpanded Light",
                (2, 3, 1, 0x409): "Regular",
                (3, 3, 1, 0x409): "2.000;FTH;Playfair-SemiExpandedLight",
                (4, 3, 1, 0x409): "Playfair SemiExpanded Light",
                (6, 3, 1, 0x409): "Playfair-SemiExpandedLight",
                (16, 3, 1, 0x409): "Playfair",
                (17, 3, 1, 0x409): "SemiExpanded Light",
            },
        ),
    ],
)
def test_name_table(fp, family_name, style_name, siblings, expected):
    font = TTFont(fp)
    siblings = [TTFont(fp) for fp in siblings]
    build_name_table(font, family_name, style_name, siblings)
    _test_names(font, expected)


def test_name_table_aggression():
    font = TTFont(mavenpro_fp)
    build_name_table(font, "Raven Am", "Regular", aggressive=True)
    _test_names(
        font,
        {
            (
                0,
                3,
                1,
                0x409,
            ): 'Copyright 2011 The Raven Am Project Authors (http://www.vissol.co.uk/mavenpro/), with Reserved Font Name "Raven Am".',
            (4, 3, 1, 0x409): "Raven Am Regular",
        },
    )
    font = TTFont(mavenpro_fp)
    build_name_table(font, "Raven Am", "Regular", aggressive=False)
    _test_names(
        font,
        {
            (
                0,
                3,
                1,
                0x409,
            ): 'Copyright 2011 The Maven Pro Project Authors (http://www.vissol.co.uk/mavenpro/), with Reserved Font Name "Maven Pro".',
            (4, 3, 1, 0x409): "Raven Am Regular",
        },
    )


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
    builder = build_fvar_instances(font, dflt_coords)
    fvar = font["fvar"]
    wght_axis = next((a for a in fvar.axes if a.axisTag == "wght"), None)
    wght_min = wght_axis.minValue
    wght_max = wght_axis.maxValue
    instances = fvar.instances
    if not dflt_coords:
        dflt_coords = {k: v["value"] for k, v in _fvar_dflts(font).items()}

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
        (wonky_fp, []),
        # don't add a linkedValue for Regular to Bold since Bold doesn't exist
        # Fixes https://github.com/googlefonts/axisregistry/issues/104
        (wavefont_fp, []),
    ],
)
def test_stat(fp, sibling_fps):
    font = TTFont(fp)
    siblings = [TTFont(f) for f in sibling_fps]
    build_stat(font, siblings)
    stat_fp = fp.replace(".ttf", "_STAT.ttx")

    ## output good files
    # with open(stat_fp, "w") as doc:
    #    got = dump(font["STAT"], font)
    #    doc.write(got)

    with open(stat_fp) as doc:
        expected = doc.read()
        got = dump(font["STAT"], font)
        assert got == expected


@pytest.mark.parametrize(
    "fp, expected",
    [
        (mavenpro_fp, "MavenPro-Regular.ttf"),
        (opensans_roman_fp, "OpenSans[wdth,wght].ttf"),
        (opensans_italic_fp, "OpenSans-Italic[wdth,wght].ttf"),
        (opensans_cond_roman_fp, "OpenSansCondensed[wght].ttf"),
        (opensans_cond_italic_fp, "OpenSansCondensed-Italic[wght].ttf"),
    ],
)
def test_filename(fp, expected):
    font = TTFont(fp)
    assert build_filename(font) == expected


@pytest.mark.parametrize(
    "fp, sibling_fps, result",
    [
        (roboto_flex_fp, [], False),
        (
            opensans_roman_fp,
            [opensans_italic_fp, opensans_cond_roman_fp, opensans_cond_italic_fp],
            True,
        ),
        (
            opensans_italic_fp,
            [opensans_roman_fp, opensans_cond_roman_fp, opensans_cond_italic_fp],
            True,
        ),
        (
            opensans_cond_roman_fp,
            [opensans_roman_fp, opensans_italic_fp, opensans_cond_italic_fp],
            True,
        ),
        (
            opensans_cond_italic_fp,
            [opensans_roman_fp, opensans_italic_fp, opensans_cond_roman_fp],
            True,
        ),
        (opensans_roman_fp, [opensans_cond_roman_fp], True),
        (opensans_roman_fp, [opensans_italic_fp], False),
        (wonky_fp, [], False),
    ],
)
def test_fvar_instance_collisions(fp, sibling_fps, result):
    ttFont = TTFont(fp)
    siblings = [TTFont(fp) for fp in sibling_fps]
    assert _fvar_instance_collisions(ttFont, siblings) == result


@pytest.mark.parametrize(
    "fp, result",
    [
        (roboto_flex_fp, "RobotoFlex"),
        (opensans_roman_fp, "OpenSans"),
        (opensans_italic_fp, "OpenSansItalic"),
        (opensans_cond_roman_fp, "OpenSansCondensed"),
        (opensans_cond_italic_fp, "OpenSansCondensedItalic"),
        (wonky_fp, "Wonky"),
    ],
)
def test_build_variations_ps_name(fp, result):
    ttFont = TTFont(fp)
    build_variations_ps_name(ttFont)
    variation_ps_name = ttFont["name"].getName(25, 3, 1, 0x409).toUnicode()
    assert variation_ps_name == result


@pytest.mark.parametrize(
    "fp, style_name, result",
    [
        (mavenpro_fp, "Regular", 400),
        (mavenpro_fp, "Italic", 400),
        (mavenpro_fp, "Black Italic", 900),
        (mavenpro_fp, "ExtraBold Italic", 800),
        (mavenpro_fp, "ExtraBold", 800),
        (mavenpro_fp, "Bold", 700),
        (mavenpro_fp, "Bold Italic", 700),
        (mavenpro_fp, "Thin Italic", 100),
        (mavenpro_fp, "Thin", 100),
    ],
)
def test_us_weight_class(fp, style_name, result):
    ttFont = TTFont(fp)
    build_name_table(ttFont, style_name=style_name)
    assert ttFont["OS/2"].usWeightClass == result
