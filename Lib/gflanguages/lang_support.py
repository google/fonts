#!/usr/bin/env python3
#
# Copyright 2022 The Google Fonts Tools Authors.
# Copyright 2017,2022 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
Helper API for interaction with languages/regions/scripts
data on the Google Fonts collection.
"""

import glob
import os

from google.protobuf import text_format
from pkg_resources import resource_filename

from gflanguages import languages_public_pb2

DATA_DIR = resource_filename("gflanguages", "data")


def LoadLanguages(languages_dir=None):
    if languages_dir is None:
        languages_dir = os.path.join(DATA_DIR, 'languages')

    langs = {}
    for textproto_file in glob.iglob(os.path.join(languages_dir, '*.textproto')):
        with open(textproto_file, 'r', encoding='utf-8') as f:
            language = text_format.Parse(f.read(), languages_public_pb2.LanguageProto())
            langs[language.id] = language
    return langs


def LoadScripts(scripts_dir=None):
    if scripts_dir is None:
        scripts_dir = os.path.join(DATA_DIR, 'scripts')

    scripts = {}
    for textproto_file in glob.iglob(os.path.join(scripts_dir, '*.textproto')):
        with open(textproto_file, 'r', encoding='utf-8') as f:
            script = text_format.Parse(f.read(), languages_public_pb2.ScriptProto())
            scripts[script.id] = script
    return scripts


def LoadRegions(regions_dir=None):
    if regions_dir is None:
        regions_dir = os.path.join(DATA_DIR, 'regions')

    regions = {}
    for textproto_file in glob.iglob(os.path.join(regions_dir, '*.textproto')):
        with open(textproto_file, 'r', encoding='utf-8') as f:
            region = text_format.Parse(f.read(), languages_public_pb2.RegionProto())
            regions[region.id] = region
    return regions
