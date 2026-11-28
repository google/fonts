name: "Afacad"
designer: "Kristian Möller, Dicotype"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-10-20"
fonts {
  name: "Afacad"
  style: "normal"
  weight: 400
  filename: "Afacad[wght].ttf"
  post_script_name: "Afacad-Regular"
  full_name: "Afacad Regular"
  copyright: "Copyright 2023 The Afacad Project Authors (https://github.com/Dicotype/Afacad)"
}
fonts {
  name: "Afacad"
  style: "italic"
  weight: 400
  filename: "Afacad-Italic[wght].ttf"
  post_script_name: "Afacad-Italic"
  full_name: "Afacad Italic"
  copyright: "Copyright 2023 The Afacad Project Authors (https://github.com/Dicotype/Afacad)"
}
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "symbols"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/Dicotype/Afacad"
  commit: "b294b1f8610ff16a3846a255b1a6a2e6788a056e"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Afacad[wght].ttf"
    dest_file: "Afacad[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Afacad-Italic[wght].ttf"
    dest_file: "Afacad-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
stroke: "SANS_SERIF"
