name: "Noto Sans Newa"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Newa"
  style: "normal"
  weight: 400
  filename: "NotoSansNewa-Regular.ttf"
  post_script_name: "NotoSansNewa-Regular"
  full_name: "Noto Sans Newa Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/newa)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "newa"
source {
  repository_url: "https://github.com/notofonts/newa"
  commit: "5a902c1fb6abf546e88d61af912d0b40f2a55de3"
  archive_url: "https://github.com/notofonts/newa/releases/download/NotoSansNewa-v2.007/NotoSansNewa-v2.007.zip"
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
    source_file: "NotoSansNewa/googlefonts/ttf/NotoSansNewa-Regular.ttf"
    dest_file: "NotoSansNewa-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-newa.yaml"
}
is_noto: true
languages: "bn_Newa"
languages: "hi_Newa"
languages: "mai_Newa"
languages: "ne_Newa"
languages: "new_Newa"
languages: "sa_Newa"
primary_script: "Newa"
