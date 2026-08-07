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
subsets: "math"
subsets: "menu"
subsets: "symbols"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/simpals/onest"
  commit: "8739b1910618a15335e4cc48842052d0ee739ade"
  archive_url: "https://github.com/simpals/onest/releases/download/2.001/onest-2.001.zip"
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
