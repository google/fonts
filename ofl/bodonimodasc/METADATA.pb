name: "Bodoni Moda SC"
designer: "Owen Earl"
license: "OFL"
category: "SERIF"
date_added: "2024-05-27"
fonts {
  name: "Bodoni Moda SC"
  style: "normal"
  weight: 400
  filename: "BodoniModaSC[opsz,wght].ttf"
  post_script_name: "BodoniModaSC-Regular"
  full_name: "Bodoni Moda SC Regular"
  copyright: "Copyright 2020 The Bodoni Moda Project Authors (https://github.com/indestructible-type/Bodoni)"
}
fonts {
  name: "Bodoni Moda SC"
  style: "italic"
  weight: 400
  filename: "BodoniModaSC-Italic[opsz,wght].ttf"
  post_script_name: "BodoniModaSC-Italic"
  full_name: "Bodoni Moda SC Italic"
  copyright: "Copyright 2020 The Bodoni Moda Project Authors (https://github.com/indestructible-type/Bodoni)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "symbols"
axes {
  tag: "opsz"
  min_value: 6.0
  max_value: 96.0
}
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 900.0
}
registry_default_overrides {
  key: "opsz"
  value: 11.0
}
source {
  repository_url: "https://github.com/indestructible-type/Bodoni"
  commit: "30ce6cdc354ef179a3b72ba0f0e71826e599348c"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BodoniModaSC[opsz,wght].ttf"
    dest_file: "BodoniModaSC[opsz,wght].ttf"
  }
  files {
    source_file: "fonts/variable/BodoniModaSC-Italic[opsz,wght].ttf"
    dest_file: "BodoniModaSC-Italic[opsz,wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
stroke: "SERIF"
