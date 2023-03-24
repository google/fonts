from gflanguages import DATA_DIR
import glob
import os
import pytest
from gflanguages import languages_public_pb2
from google.protobuf import text_format


languages_dir = os.path.join(DATA_DIR, "languages")
textproto_files = [os.path.basename(x) for x in glob.iglob(os.path.join(languages_dir, "*.textproto"))]

@pytest.mark.parametrize("lang_code", textproto_files)
def test_parsable(lang_code):
    with open(os.path.join(languages_dir, lang_code), "r", encoding="utf-8") as f:
        text_format.Parse(f.read(), languages_public_pb2.LanguageProto())
