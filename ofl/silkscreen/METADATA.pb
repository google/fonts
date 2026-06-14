name: "Silkscreen"
designer: "Jason Kottke"
license: "OFL"
category: "DISPLAY"
date_added: "2022-06-23"
fonts {
  name: "Silkscreen"
  style: "normal"
  weight: 400
  filename: "Silkscreen-Regular.ttf"
  post_script_name: "Silkscreen-Regular"
  full_name: "Silkscreen Regular"
  copyright: "Copyright 2001 The Silkscreen Project Authors (https://github.com/googlefonts/silkscreen)"
}
fonts {
  name: "Silkscreen"
  style: "normal"
  weight: 700
  filename: "Silkscreen-Bold.ttf"
  post_script_name: "Silkscreen-Bold"
  full_name: "Silkscreen Bold"
  copyright: "Copyright 2001 The Silkscreen Project Authors (https://github.com/googlefonts/silkscreen)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/googlefonts/silkscreen"
  commit: "206ccf3f5234c281461e63ecc59cbc6b0563472b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Silkscreen-Regular.ttf"
    dest_file: "Silkscreen-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/Silkscreen-Bold.ttf"
    dest_file: "Silkscreen-Bold.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
stroke: "SANS_SERIF"
classifications: "DISPLAY"
