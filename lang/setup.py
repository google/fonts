# coding: utf-8
#
# Copyright 2022 The Google Fonts Tools Authors.
# Copyright 2017,2022 Google LLC All Rights Reserved.
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
with open('README.md') as f:
    long_description = f.read()

setup(
    name="gflanguages",
    use_scm_version={"write_to": "Lib/gflanguages/_version.py"},
    url='https://github.com/googlefonts/lang/',
    description='A python API for evaluating language support in the Google Fonts collection.',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    author=('Dave Crossland, '
            'Felipe Sanches, '
            'Marc Foley, '
            'Roderick Sheeter'),
    author_email='dave@lab6.com',
    package_dir={'': 'Lib'},
    packages=['gflanguages'],
    package_data={'gflanguages': [
                     "data/languages/*.textproto",
                     "data/regions/*.textproto",
                     "data/scripts/*.textproto"
                 ]
    },
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Fonts',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    python_requires=">=3.7",
    setup_requires=['setuptools_scm'],
    install_requires=[
        # 3.7.0 fixed a bug on parsing some METADATA.pb files.
        # We cannot use v4 because our protobuf files have been compiled with v3.
        'protobuf>=3.7.0, <4',
    ]
)
