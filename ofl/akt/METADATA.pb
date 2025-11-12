name: "Akt"
designer: "Dima Grenev"
license: "OFL"
category: "SANS_SERIF"
date_added: "2025-11-12"
fonts {
  name: "Akt"
  style: "normal"
  weight: 400
  filename: "Akt[wght].ttf"
  post_script_name: "Akt-Regular"
  full_name: "Akt Regular"
  copyright: "Copyright 2024 The Akt Project Authors (https://github.com/dimgrenev/akt)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 0.0
  max_value: 1000.0
  default_value: 400.0
}
source {
  repository_url: "https://github.com/dimgrenev/akt"
  commit: "d166132d90f3f01351e3def962e5d0fd5399deab"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Akt[wght].ttf"
    dest_file: "Akt[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
primary_script: "Latn"