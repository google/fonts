name: "Noto Sans Balinese"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Balinese"
  style: "normal"
  weight: 400
  filename: "NotoSansBalinese[wght].ttf"
  post_script_name: "NotoSansBalinese-Regular"
  full_name: "Noto Sans Balinese Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/balinese)"
}
subsets: "balinese"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/notofonts/balinese"
  commit: "e6c2d4c19072cb6da80d74ad9f683b749f5b6f00"
  archive_url: "https://github.com/notofonts/balinese/releases/download/NotoSansBalinese-v2.006/NotoSansBalinese-v2.006.zip"
  config_yaml: "sources/config-sans-balinese.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansBalinese/googlefonts/variable-ttf/NotoSansBalinese[wght].ttf"
    dest_file: "NotoSansBalinese[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "ban_Bali"  # Balinese, Balinese
languages: "sa_Bali"  # Sanskrit, Balinese
primary_script: "Bali"
