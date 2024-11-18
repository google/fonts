import glob
import os
import pytest
import sys
from gflanguages import languages_public_pb2
from google.protobuf import text_format

if sys.version_info < (3, 10):
    from importlib_resources import files
else:
    from importlib.resources import files

languages_dir = files("gflanguages.data").joinpath("languages")
textproto_files = [
    file.name for file in languages_dir.iterdir() if file.name.endswith(".textproto")
]


@pytest.mark.parametrize("lang_code", textproto_files)
def test_parsable(lang_code):
    f = languages_dir.joinpath(lang_code)
    msg = text_format.Parse(
        f.read_text(encoding="utf-8"), languages_public_pb2.LanguageProto()
    )
    assert msg.id
    assert msg.language
    assert msg.script
    assert msg.population is not None
