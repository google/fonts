name: "Noto Sans Cypriot"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Cypriot"
  style: "normal"
  weight: 400
  filename: "NotoSansCypriot-Regular.ttf"
  post_script_name: "NotoSansCypriot-Regular"
  full_name: "Noto Sans Cypriot Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/cypriot)"
}
subsets: "cypriot"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/cypriot"
  commit: "4f81293d17d7b3c9c67b9ab2c335905c75ad3f1d"
  archive_url: "https://github.com/notofonts/cypriot/releases/download/NotoSansCypriot-v2.002/NotoSansCypriot-v2.002.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansCypriot/googlefonts/ttf/NotoSansCypriot-Regular.ttf"
    dest_file: "NotoSansCypriot-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-cypriot.yaml"
}
is_noto: true
languages: "grc_Cprt"
primary_script: "Cprt"
