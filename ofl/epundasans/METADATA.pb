name: "Epunda Sans"
designer: "Typofactur"
license: "OFL"
category: "SANS_SERIF"
date_added: "2025-03-21"
fonts {
  name: "Epunda Sans"
  style: "normal"
  weight: 400
  filename: "EpundaSans[wght].ttf"
  post_script_name: "EpundaSans-Light"
  full_name: "Epunda Sans Light"
  copyright: "Copyright 2024 The Epunda Sans Project Authors (https://github.com/typofactur/epundasans.git)"
}
fonts {
  name: "Epunda Sans"
  style: "italic"
  weight: 400
  filename: "EpundaSans-Italic[wght].ttf"
  post_script_name: "EpundaSans-LightItalic"
  full_name: "Epunda Sans Light Italic"
  copyright: "Copyright 2024 The Epunda Sans Project Authors (https://github.com/typofactur/epundasans.git)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/typofactur/epundasans"
  commit: "4a75d7da519ebed2c580e024a3e447a6bde69377"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/EpundaSans[wght].ttf"
    dest_file: "EpundaSans[wght].ttf"
  }
  files {
    source_file: "fonts/variable/EpundaSans-Italic[wght].ttf"
    dest_file: "EpundaSans-Italic[wght].ttf"
  }
  branch: "main"
}
stroke: "SANS_SERIF"
