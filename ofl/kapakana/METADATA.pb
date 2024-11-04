name: "Kapakana"
designer: "Kousuke Nagai"
license: "OFL"
category: "HANDWRITING"
date_added: "2020-12-21"
fonts {
  name: "Kapakana"
  style: "normal"
  weight: 400
  filename: "Kapakana[wght].ttf"
  post_script_name: "Kapakana-Regular"
  full_name: "Kapakana Regular"
  copyright: "Copyright 2020 The Kapakana Project Authors (https://github.com/nagamaki008/kapakana)"
}
subsets: "japanese"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 400.0
}
source {
  repository_url: "https://github.com/nagamaki008/kapakana"
  files {
    source_file: "fonts/ttf/Kapakana-Light.ttf"
    dest_file: "static/Kapakana-Light.ttf"
  }
  files {
    source_file: "fonts/ttf/Kapakana-Regular.ttf"
    dest_file: "static/Kapakana-Regular.ttf"
  }
  files {
    source_file: "fonts/variable/Kapakana[wght].ttf"
    dest_file: "Kapakana[wght].ttf"
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
classifications: "DISPLAY"
classifications: "HANDWRITING"
