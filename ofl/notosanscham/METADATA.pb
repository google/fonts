name: "Noto Sans Cham"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Cham"
  style: "normal"
  weight: 400
  filename: "NotoSansCham[wght].ttf"
  post_script_name: "NotoSansCham-Regular"
  full_name: "Noto Sans Cham Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/cham)"
}
subsets: "cham"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/cham"
  commit: "ab48c582e3c834028dc0444b832874be83532350"
  archive_url: "https://github.com/notofonts/cham/releases/download/NotoSansCham-v2.005/NotoSansCham-v2.005.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "NotoSansCham/googlefonts/variable-ttf/NotoSansCham[wght].ttf"
    dest_file: "NotoSansCham[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-cham.yaml"
}
is_noto: true
languages: "cja_Cham"
languages: "cjm_Cham"
languages: "sa_Cham"
primary_script: "Cham"
