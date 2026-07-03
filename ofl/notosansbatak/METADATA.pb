name: "Noto Sans Batak"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Batak"
  style: "normal"
  weight: 400
  filename: "NotoSansBatak-Regular.ttf"
  post_script_name: "NotoSansBatak-Regular"
  full_name: "Noto Sans Batak Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/batak)"
}
subsets: "batak"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/batak"
  commit: "139c2a6c256d72c560f894569c799d6bf090ba72"
  archive_url: "https://github.com/notofonts/batak/releases/download/NotoSansBatak-v2.005/NotoSansBatak-v2.005.zip"
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
    source_file: "NotoSansBatak/googlefonts/ttf/NotoSansBatak-Regular.ttf"
    dest_file: "NotoSansBatak-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-batak.yaml"
}
is_noto: true
languages: "bbc_Batk"  # Batak Toba, Batak
primary_script: "Batk"
