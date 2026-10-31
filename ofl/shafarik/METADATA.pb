name: "Shafarik"
designer: "Aleksandr Andreev"
license: "OFL"
category: "DISPLAY"
date_added: "2024-12-06"
fonts {
  name: "Shafarik"
  style: "normal"
  weight: 400
  filename: "Shafarik-Regular.ttf"
  post_script_name: "Shafarik-Regular"
  full_name: "Shafarik Regular"
  copyright: "Copyright 2025 The Shafarik Project Authors (https://github.com/slavonic/Shafarik.git)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "glagolitic"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/slavonic/shafarik"
  commit: "e4045d59b275755b2b8532b201402786055466d8"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Shafarik-Regular.ttf"
    dest_file: "Shafarik-Regular.ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
primary_script: "Cyrl"
