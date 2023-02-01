# coding: utf-8
#
# Copyright 2022 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# See AUTHORS.txt for the list of Authors and LICENSE.txt for the License.
from setuptools import setup

# Read the contents of the README file
with open("README.md") as f:
    long_description = f.read()

setup(
    name="axisregistry",
    use_scm_version={"write_to": "Lib/axisregistry/_version.py"},
    url="https://github.com/googlefonts/axisregistry/",
    description="A python API to access data from the Google Fonts variable fonts axis registry.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # This is important!
    author=("Felipe Sanches"),
    author_email="juca@members.fsf.org",
    package_dir={"": "Lib"},
    packages=["axisregistry"],
    package_data={"axisregistry": ["data/*.textproto"]},
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Fonts",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
    setup_requires=[
        "setuptools>=61.2",
        "setuptools_scm[toml]>=6.2",
    ],
    install_requires=["protobuf>=3.19.4, <4", "fonttools"],
)
