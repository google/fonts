name: "Rubik"
designer: "Hubert and Fischer, Meir Sadan, Cyreal, Daniel Grumer, Omaima Dajani"
license: "OFL"
category: "SANS_SERIF"
date_added: "2015-07-22"
fonts {
  name: "Rubik"
  style: "normal"
  weight: 400
  filename: "Rubik[wght].ttf"
  post_script_name: "Rubik-Light"
  full_name: "Rubik Light"
  copyright: "Copyright 2015 The Rubik Project Authors (https://github.com/googlefonts/rubik)"
}
fonts {
  name: "Rubik"
  style: "italic"
  weight: 400
  filename: "Rubik-Italic[wght].ttf"
  post_script_name: "Rubik-LightItalic"
  full_name: "Rubik Light Italic"
  copyright: "Copyright 2015 The Rubik Project Authors (https://github.com/googlefonts/rubik)"
}
subsets: "arabic"
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "hebrew"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/googlefonts/rubik"
  commit: "e337a5f69a9bea30e58d05bd40184d79cc099628"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Rubik-Italic[wght].ttf"
    dest_file: "Rubik-Italic[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Rubik[wght].ttf"
    dest_file: "Rubik[wght].ttf"
  }
  branch: "main"
}
