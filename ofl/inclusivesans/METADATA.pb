name: "Inclusive Sans"
designer: "Olivia King"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-08-04"
fonts {
  name: "Inclusive Sans"
  style: "normal"
  weight: 400
  filename: "InclusiveSans[wght].ttf"
  post_script_name: "InclusiveSans-Regular"
  full_name: "Inclusive Sans Regular"
  copyright: "Copyright 2024 The Inclusive Sans Project Authors (https://github.com/LivKing/Inclusive-Sans)"
}
fonts {
  name: "Inclusive Sans"
  style: "italic"
  weight: 400
  filename: "InclusiveSans-Italic[wght].ttf"
  post_script_name: "InclusiveSans-Italic"
  full_name: "Inclusive Sans Italic"
  copyright: "Copyright 2024 The Inclusive Sans Project Authors (https://github.com/LivKing/Inclusive-Sans)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/LivKing/Inclusive-Sans"
  commit: "38b8ed1dd67bd25ef4180140492810cf050ef501"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/InclusiveSans[wght].ttf"
    dest_file: "InclusiveSans[wght].ttf"
  }
  files {
    source_file: "fonts/variable/InclusiveSans-Italic[wght].ttf"
    dest_file: "InclusiveSans-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
primary_script: "Zinh"
