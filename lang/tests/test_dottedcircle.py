import uharfbuzz as hb
import gflanguages
import pytest

langs = gflanguages.LoadLanguages()
xfail_langs = {"kkh_Lana": "Tai Tham encoding is over-differentiated (see L2/19-365)"}


@pytest.fixture
def hb_font():
    # Persuade Harfbuzz we have a font that supports
    # every codepoint.
    face = hb.Face(b"")
    font = hb.Font(face)
    funcs = hb.FontFuncs.create()
    funcs.set_nominal_glyph_func((lambda font, cp, data: cp), None)
    font.funcs = funcs
    return font


@pytest.mark.parametrize("lang", langs.keys())
def test_dotted_circle(lang, hb_font):
    if lang in xfail_langs:
        pytest.xfail("Language is expected to fail: " + xfail_langs[lang])
    item = langs[lang]
    samples = item.sample_text.ListFields()
    for sample_name, sample in sorted(samples, key=lambda x: len(x[1])):
        buf = hb.Buffer()
        buf.add_str(sample)
        buf.guess_segment_properties()
        hb.shape(hb_font, buf)
        ok = not any(info.codepoint == 0x25CC for info in buf.glyph_infos)
        assert ok, f"Dotted circle found in {sample} ({lang}.{sample_name.name})"
