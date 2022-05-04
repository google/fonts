from fontTools.ttLib import TTFont
from axisregistry import GFNameBuilder
import pytest
import os

CWD = os.path.dirname(__file__)

@pytest.fixture
def static_font():
    fp = os.path.join(CWD, "data", "MavenPro-Regular.ttf")
    return TTFont(fp)

def _test_names(ttFont, expected):
    name_table = ttFont["name"]
    for k, v in expected.items():
        record = name_table.getName(*k)
        if not record:
            assert record == v, f"{k} record is incorrect, expected {v} got {record}"
        else:
            record_string = record.toUnicode()
            assert record_string == v, f"{k} record is incorrect, expected {v} got {record}" 



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
    ]
)
def test_static_name_table(static_font, family_name, style_name, expected):
    builder = GFNameBuilder(static_font)
    builder.build_name_table(family_name, style_name)
    _test_names(static_font, expected)
