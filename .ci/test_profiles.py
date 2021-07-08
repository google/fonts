import pytest
import sys
import os
from bs4 import BeautifulSoup
import requests
from fontbakery.designers_pb2 import DesignerInfoProto
from google.protobuf import text_format


# TODO this could potentially be a fontbakery profile


@pytest.fixture
def profile_dir():
    if len(sys.argv) != 3:
        print("Usage: python test_profiles fonts/catalog/designers/designerprofile")
        sys.exit(1)
    return sys.argv[-1]


@pytest.fixture
def proto_info(profile_dir):
    info_file = os.path.join(profile_dir, "info.pb")
    with open(info_file, "rb") as info:
        text = info.read()
    return load_info_proto(text)


@pytest.fixture
def bio(profile_dir):
    bio_file = os.path.join(profile_dir, "bio.html")
    with open(bio_file) as html:
        return BeautifulSoup(html.read(), features="lxml")


def load_info_proto(text_data):
    message = DesignerInfoProto()
    text_format.Merge(text_data, message)
    return message


def test_profile_dir_exists(profile_dir):
    assert os.path.exists(profile_dir)


def test_profile_dir_has_bio(profile_dir):
    assert "bio.html" in os.listdir(profile_dir), "bio.html is missing"


def test_profile_dir_has_info(profile_dir):
    assert "info.pb" in os.listdir(profile_dir), "info.pb is missing"


def test_profile_has_correct_img(profile_dir):
    assert not any(f for f in os.listdir(profile_dir) if f.endswith((".jpg", ".jpeg")))
    assert any(
        f for f in os.listdir(profile_dir) if f.endswith(".png")
    ), "Profile is missing png image"


def test_profile_info_image_link_is_correct(profile_dir, proto_info):
    img_path = proto_info.avatar.file_name
    assert img_path in os.listdir(profile_dir), "info.pb: image path is incorrect"


def test_info_link(proto_info):
    link = proto_info.link
    assert (
        "plus.google" not in link
    ), "Google+ links are no longer supported. Please replace."


def test_info_link_works(proto_info):
    link = proto_info.link
    if "instagram.com" in link or not link:
        return
    assert requests.get(link).status_code == 200, "info.pb: link is not producing a 200 status code"


def test_bio_links_work(bio):
    urls = bio.find_all("a", href=True)
    urls = [u["href"] for u in urls]
    for url in urls:
        if "instagram.com" in url:  # these have a habit of raise a 4xx status code
            continue
        assert (
            requests.get(url).status_code == 200
        ), f"{url} is not producing a 200 status code"
