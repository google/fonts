name: "Noto Sans Runic"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Runic"
  style: "normal"
  weight: 400
  filename: "NotoSansRunic-Regular.ttf"
  post_script_name: "NotoSansRunic-Regular"
  full_name: "Noto Sans Runic Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/runic)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "runic"
source {
  repository_url: "https://github.com/notofonts/runic"
  commit: "0badcd990e0be2e6010362488af5a901a7bfefa1"
  archive_url: "https://github.com/notofonts/runic/releases/download/NotoSansRunic-v2.002/NotoSansRunic-v2.002.zip"
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
    source_file: "NotoSansRunic/googlefonts/ttf/NotoSansRunic-Regular.ttf"
    dest_file: "NotoSansRunic-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-runic.yaml"
}
is_noto: true
languages: "de_Runr"
languages: "got_Runr"
languages: "non_Runr"
primary_script: "Runr"
