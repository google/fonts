name: "Chivo"
designer: "Omnibus-Type"
license: "OFL"
category: "SANS_SERIF"
date_added: "2011-12-07"
fonts {
  name: "Chivo"
  style: "normal"
  weight: 400
  filename: "Chivo[wght].ttf"
  post_script_name: "Chivo-Medium"
  full_name: "Chivo Medium"
  copyright: "Copyright 2019 The Chivo Project Authors (https://github.com/Omnibus-Type/Chivo)"
}
fonts {
  name: "Chivo"
  style: "italic"
  weight: 400
  filename: "Chivo-Italic[wght].ttf"
  post_script_name: "Chivo-MediumItalic"
  full_name: "Chivo Medium Italic"
  copyright: "Copyright 2019 The Chivo Project Authors (https://github.com/Omnibus-Type/Chivo)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/Omnibus-Type/Chivo"
  commit: "dc61c468d79781eb5183426e88e844af16cdc3e5"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Chivo/variable/Chivo[wght].ttf"
    dest_file: "Chivo[wght].ttf"
  }
  files {
    source_file: "fonts/Chivo/variable/Chivo-Italic[wght].ttf"
    dest_file: "Chivo-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
