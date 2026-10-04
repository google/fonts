name: "Noto Sans Mongolian"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Mongolian"
  style: "normal"
  weight: 400
  filename: "NotoSansMongolian-Regular.ttf"
  post_script_name: "NotoSansMongolian-Regular"
  full_name: "Noto Sans Mongolian Regular"
  copyright: "Copyright 2023 The Noto Project Authors (https://github.com/notofonts/mongolian)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "mongolian"
subsets: "symbols"
source {
  repository_url: "https://github.com/notofonts/mongolian"
  commit: "a61ef47935dcf4e4675456b632d6248836a5496a"
  archive_url: "https://github.com/notofonts/mongolian/releases/download/NotoSansMongolian-v3.002/NotoSansMongolian-v3.002.zip"
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansMongolian/googlefonts/ttf/NotoSansMongolian-Regular.ttf"
    dest_file: "NotoSansMongolian-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-mongolian.yaml"
}
is_noto: true
languages: "mn_Mong"
languages: "mnc_Mong"
languages: "sa_Mong"
primary_script: "Mong"
