name: "Gantari"
designer: "Lafontype"
license: "OFL"
category: "SANS_SERIF"
date_added: "2022-05-26"
fonts {
  name: "Gantari"
  style: "normal"
  weight: 400
  filename: "Gantari[wght].ttf"
  post_script_name: "Gantari-Regular"
  full_name: "Gantari Regular"
  copyright: "Copyright 2022 The Gantari Project Authors (https://github.com/Lafontype/Gantari)"
}
fonts {
  name: "Gantari"
  style: "italic"
  weight: 400
  filename: "Gantari-Italic[wght].ttf"
  post_script_name: "Gantari-Italic"
  full_name: "Gantari Italic"
  copyright: "Copyright 2022 The Gantari Project Authors (https://github.com/Lafontype/Gantari)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/Lafontype/Gantari"
  commit: "363a3dd5634bfec7e9f7db11ca3e1f4739a182ab"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Gantari[wght].ttf"
    dest_file: "Gantari[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Gantari-Italic[wght].ttf"
    dest_file: "Gantari-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
