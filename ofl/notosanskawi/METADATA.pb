name: "Noto Sans Kawi"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-06-28"
fonts {
  name: "Noto Sans Kawi"
  style: "normal"
  weight: 400
  filename: "NotoSansKawi[wght].ttf"
  post_script_name: "NotoSansKawi-Regular"
  full_name: "Noto Sans Kawi Regular"
  copyright: "Copyright 2023 The Noto Project Authors (https://github.com/notofonts/kawi)"
}
subsets: "kawi"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/notofonts/kawi"
  commit: "7b1182376580f1192b0ac9cc172ee1ee723655b7"
  archive_url: "https://github.com/notofonts/kawi/releases/download/NotoSansKawi-v1.000/NotoSansKawi-v1.000.zip"
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
    source_file: "NotoSansKawi/googlefonts/variable-ttf/NotoSansKawi[wght].ttf"
    dest_file: "NotoSansKawi[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-kawi.yaml"
}
is_noto: true
languages: "kaw_Kawi"
primary_script: "Kawi"
