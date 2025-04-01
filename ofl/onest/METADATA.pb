name: "Onest"
designer: "Dmitri Voloshin, Andrey Kudryavtsev"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-09-06"
fonts {
  name: "Onest"
  style: "normal"
  weight: 400
  filename: "Onest[wght].ttf"
  post_script_name: "Onest-Regular"
  full_name: "Onest Regular"
  copyright: "Copyright 2021 The Onest Project Authors (https://github.com/simpals/onest)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/simpals/onest"
  commit: "f18c06a14512e43a6191849278d6f07fdaf347d6"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Onest[wght].ttf"
    dest_file: "Onest[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
