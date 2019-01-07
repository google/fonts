"""Generate before and after gifs using diffbrowsers. Upload them to imgur then post them to PR"""
import os
import shutil
import requests
import json
from zipfile import ZipFile
import subprocess
from uuid import uuid4


REPORT_DIR = 'out'
GFR_URL = 'http://159.65.243.73'


def post_media_to_gfr(paths, uuid):
    """Post images to GF Regression"""
    url_endpoint = GFR_URL + '/api/upload-media'
    payload = [('files', open(path, 'rb')) for path in paths]
    r = requests.post(
        url_endpoint,
        data={'uuid': uuid},
        files=payload,
        headers={"Access-Token": os.environ["GFR_TOKEN"]}
    )
    return [os.path.join(GFR_URL, i) for i in r.json()['items']]


def post_gh_msg(msg):
    r = requests.post("https://api.github.com/repos/{}/issues/{}/comments".format(os.environ['TRAVIS_REPO_SLUG'], os.environ['TRAVIS_PULL_REQUEST']),
        data=json.dumps({'body': msg}),
        headers={'Authorization': 'token {}'.format(os.environ['GH_TOKEN'])})
    print(r.text)


def get_fonts_in_pr():
    font_paths = []
    r = requests.get("https://api.github.com/repos/{}/pulls/{}/files".format(os.environ['TRAVIS_REPO_SLUG'], os.environ['TRAVIS_PULL_REQUEST']),
        headers={'Authorization': 'token {}'.format(os.environ['GH_TOKEN'])})
    for item in r.json():
        if item['filename'].endswith('.ttf'):
            font_paths.append(item['filename'])
    return font_paths


def find_files(directory, ext='.gif'):
    """Recurs through directory and return files which have the given extension"""
    found_files = []
    for path, r, files in os.walk(directory):
        for f in files:
            if not f.endswith(ext):
                continue
            found_files.append(os.path.join(path, f))
    return found_files


def main():
    fonts_after = get_fonts_in_pr()
    subprocess.call(["gftools", "qa"] + \
                    fonts_after + \
                    ["-a", "-o", REPORT_DIR])
    report_zip = shutil.make_archive("out", 'zip', REPORT_DIR)
    uuid = str(uuid4())
    zip_url = post_media_to_gfr([report_zip], uuid)
    msg = "Diff images: {}".format(zip_url[0])
    post_gh_msg(msg)


if __name__ == '__main__':
    main()
