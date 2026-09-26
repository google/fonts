name: "Noto Serif Balinese"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Balinese"
  style: "normal"
  weight: 400
  filename: "NotoSerifBalinese-Regular.ttf"
  post_script_name: "NotoSerifBalinese-Regular"
  full_name: "Noto Serif Balinese Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/balinese)"
}
subsets: "balinese"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/balinese"
  commit: "3677ecce1289bdd0014392c8ef878ba972b93bb0"
  archive_url: "https://github.com/notofonts/balinese/releases/download/NotoSerifBalinese-v2.007/NotoSerifBalinese-v2.007.zip"
  config_yaml: "sources/config-serif-balinese.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSerifBalinese/googlefonts/ttf/NotoSerifBalinese-Regular.ttf"
    dest_file: "NotoSerifBalinese-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "ban_Bali"  # Balinese, Balinese
languages: "sa_Bali"  # Sanskrit, Balinese
primary_script: "Bali"
