#!/usr/bin/env python
# Copyright 2015, Google Inc.
# Author: Dave Crossland (dave@understandinglimited.com)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# namelist.py: A fontTools python script for generating namelist files
#
# Usage:
#
#   $ namelist.py Font.ttf > NameList.nam
import sys
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

def main(file_name):
    excluded_chars = ["????", "SPACE", "NO-BREAK SPACE"]
    font = TTFont(file_name)
    for cmap in font["cmap"].tables: 
        char_list = sorted(cmap.cmap.items())
        for item in char_list:
            item_description = Unicode[item[0]]
            if item_description not in excluded_chars:
                print hex(item[0]), item_description
    font.close()

if __name__ == '__main__':
    main(sys.argv[1])
