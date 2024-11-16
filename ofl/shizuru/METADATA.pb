name: "Shizuru"
designer: "Shibuya Font"
license: "OFL"
category: "DISPLAY"
date_added: "2020-12-08"
fonts {
  name: "Shizuru"
  style: "normal"
  weight: 400
  filename: "Shizuru-Regular.ttf"
  post_script_name: "Shizuru-Regular"
  full_name: "Shizuru Regular"
  copyright: "Copyright 2020 The Shizuru Project Authors (https://github.com/shibuyafont/shizuru-font), all rights reserved."
}
subsets: "japanese"
subsets: "latin"
subsets: "menu"
source {
  repository_url: "https://github.com/shibuyafont/shizuru-font"
  files {
    source_file: "fonts/ttf/ShizuruFont-Regular.ttf"
    dest_file: "Shizuru-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
languages: "ja_Kana"  # Japanese, Katakana
languages: "ja_Hira"  # Japanese, Hiragana
primary_script: "Hira"
