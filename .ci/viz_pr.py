"""Generate before and after gifs using diffbrowsers. Upload them to imgur then post them to PR"""
import os
import shutil
import requests
import json
from zipfile import ZipFile
import subprocess
from uuid import uuid4
import logging

logging.getLogger().setLevel(logging.INFO)

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


def post_gh_msg(msg, repo_slug=None, pull_id=None):
    pull_id = pull_id if pull_id else os.environ['TRAVIS_PULL_REQUEST']
    repo_slug = repo_slug if repo_slug else os.environ['TRAVIS_REPO_SLUG']
    r = requests.post("https://api.github.com/repos/{}/issues/{}/comments".format(repo_slug, pull_id),
        data=json.dumps({'body': msg}),
        headers={'Authorization': 'token {}'.format(os.environ['GH_TOKEN'])})
    print(r.text)


def get_fonts_in_pr(repo_slug=None, pull_id=None):
    font_paths = []
    pull_id = pull_id if pull_id else os.environ['TRAVIS_PULL_REQUEST']
    repo_slug = repo_slug if repo_slug else os.environ['TRAVIS_REPO_SLUG']
    r = requests.get("https://api.github.com/repos/{}/pulls/{}/files".format(repo_slug, str(pull_id)),
        headers={'Authorization': 'token {}'.format(os.environ['GH_TOKEN'])})
    for item in r.json():
        filename = item['filename']
        if filename.endswith('.ttf'):
            if len(os.path.normpath(filename).split(os.path.sep)) > 3:
                continue
            font_paths.append(filename)
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


def sep_fonts_into_families(fonts):
    families= {}
    for font in fonts:
        family = os.path.basename(font).split("-")[0]
        if family not in families:
            families[family] = []
        families[family].append(font)
    return families


def main():
    fonts_after = get_fonts_in_pr()
    if not fonts_after:
        post_gh_msg("No fonts found. Skipping font QA")
        return
    families = sep_fonts_into_families(fonts_after)
    for family, fonts in families.items():
        family_qa_dir = "{}_qa".format(family)
        subprocess.call(["gftools", "qa"] + \
                        fonts + \
                        ["-a", "-o", family_qa_dir])
        # upload QA zip to GFRegression
        report_zip = shutil.make_archive(family_qa_dir, "zip", family_qa_dir)
        uuid = str(uuid4())
        zip_url = post_media_to_gfr([report_zip], uuid)
        msg = "{} Diff images: [{}.zip]({})".format(family, family_qa_dir, zip_url[0])
        # TODO (M Foley as FB report and diff report)
        post_gh_msg(msg)


if __name__ == '__main__':
    main()

