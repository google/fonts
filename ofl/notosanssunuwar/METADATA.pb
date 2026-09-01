name: "Noto Sans Sunuwar"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2025-06-11"
fonts {
  name: "Noto Sans Sunuwar"
  style: "normal"
  weight: 400
  filename: "NotoSansSunuwar-Regular.ttf"
  post_script_name: "NotoSansSunuwar-Regular"
  full_name: "Noto Sans Sunuwar Regular"
  copyright: "Copyright 2021 The Noto Sunuwar Project Authors (https://github.com/ScriptEncodingInitiative/sunuwar)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "sunuwar"
source {
  repository_url: "https://github.com/notofonts/sunuwar"
  commit: "981b7c03c93f203c838b280c232de9166e8fb8c6"
  archive_url: "https://github.com/notofonts/sunuwar/releases/download/NotoSansSunuwar-v1.000/NotoSansSunuwar-v1.000.zip"
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
    source_file: "NotoSansSunuwar/googlefonts/ttf/NotoSansSunuwar-Regular.ttf"
    dest_file: "NotoSansSunuwar-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-sunuwar.yaml"
}
is_noto: true
languages: "suz_Sunu"
primary_script: "Sunu"
