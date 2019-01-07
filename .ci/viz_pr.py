"""Run gftools qa in travis on new/modified fonts and output results
as message in PR."""
import os
import re
import shutil
import requests
import json
from zipfile import ZipFile
import subprocess
from fontTools.ttLib import TTFont
from uuid import uuid4
import logging

logging.getLogger().setLevel(logging.INFO)

GFR_URL = 'http://35.188.158.120/'


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


def get_fonts_in_pr(repo_slug=None, pull_id=None):
    font_paths = []
    pull_id = pull_id if pull_id else os.environ['TRAVIS_PULL_REQUEST']
    repo_slug = repo_slug if repo_slug else os.environ['TRAVIS_REPO_SLUG']
    api_url = "https://api.github.com/repos/{}/pulls/{}/files?page={}&per_page=30"

    # Find last api page
    r = requests.get(api_url.format(repo_slug, str(pull_id), "1"),
        headers={'Authorization': 'token {}'.format(os.environ['GH_TOKEN'])})
    if 'link' in r.headers:
        pages = re.search(
            r'(?<=page\=)[0-9]{1,5}(?<!\&per_page=50\>\; rel="last")',
            r.headers['link']).group(0)
    else:
        pages = 1

    for page in range(1, int(pages) + 1):
        r = requests.get(api_url.format(repo_slug, str(pull_id), page),
            headers={'Authorization': 'token {}'.format(os.environ['GH_TOKEN'])})
        for item in r.json():
            filename = item['filename']
            if filename.endswith('.ttf') and item['status'] != 'removed':
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


def fonts_have_multiple_axes(ttfonts):
    for ttfont in ttfonts:
        if 'fvar' not in ttfont:
            continue
        if len(ttfont['fvar'].axes) > 1:
            return True
    return False


def main():
    fonts_after = get_fonts_in_pr()
    if not fonts_after:
        post_gh_msg("No fonts found. Skipping font QA")
        return
    families = sep_fonts_into_families(fonts_after)
    if len(families) > 1:
        post_gh_msg(("Aborting QA. PR contains {} families. "
                     "Please pr them individually.").format(len(families)))
        return
    ttfonts = [TTFont(f) for f in fonts_after]
    if fonts_have_multiple_axes(ttfonts):
        post_gh_msg("Aborting QA. Fonts have more than one vf axis")
        return

    family_qa_dir = "qa"
    subprocess.call(["gftools", "qa"] + \
                    fonts_after + \
                    ["-a", "-o", family_qa_dir])
    # upload QA zip to GFRegression
    report_zip = shutil.make_archive(family_qa_dir, "zip", family_qa_dir)
    uuid = str(uuid4())
    zip_url = post_media_to_gfr([report_zip], uuid)
    with open(os.path.join(family_qa_dir, "Fontbakery", "report.md"), "r") as fb:
        msg = "{}\n\n## Diff images: [{}.zip]({})".format(
            fb.read(), family_qa_dir, zip_url[0])
        post_gh_msg(msg)


if __name__ == '__main__':
    main()

