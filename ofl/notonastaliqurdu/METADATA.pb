name: "Noto Nastaliq Urdu"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Nastaliq Urdu"
  style: "normal"
  weight: 400
  filename: "NotoNastaliqUrdu[wght].ttf"
  post_script_name: "NotoNastaliqUrdu-Regular"
  full_name: "Noto Nastaliq Urdu Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/nastaliq)"
}
subsets: "arabic"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/notofonts/nastaliq"
  commit: "3508acd351a8603c6b74d2cff2da66b0806374d1"
  archive_url: "https://github.com/notofonts/nastaliq/releases/download/NotoNastaliqUrdu-v3.009/NotoNastaliqUrdu-v3.009.zip"
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
    source_file: "NotoNastaliqUrdu/googlefonts/variable/NotoNastaliqUrdu[wght].ttf"
    dest_file: "NotoNastaliqUrdu[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config-nastaliq-urdu.yaml"
}
is_noto: true
languages: "ur_Arab"
primary_script: "Arab"
