name: "Funnel Sans"
designer: "NORD ID, Kristian Möller"
license: "OFL"
category: "SANS_SERIF"
date_added: "2024-09-27"
fonts {
  name: "Funnel Sans"
  style: "normal"
  weight: 400
  filename: "FunnelSans[wght].ttf"
  post_script_name: "FunnelSans-Light"
  full_name: "Funnel Sans Light"
  copyright: "Copyright 2023 The Funnel Project Authors (https://github.com/Dicotype/Funnel)"
}
fonts {
  name: "Funnel Sans"
  style: "italic"
  weight: 400
  filename: "FunnelSans-Italic[wght].ttf"
  post_script_name: "FunnelSans-LightItalic"
  full_name: "Funnel Sans Light Italic"
  copyright: "Copyright 2023 The Funnel Project Authors (https://github.com/Dicotype/Funnel)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 800.0
}
source {
  repository_url: "https://github.com/Dicotype/Funnel"
  commit: "f9509ce0df3c344ddc454600baf77df54b83c379"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Funnel_Sans/variable/FunnelSans[wght].ttf"
    dest_file: "FunnelSans[wght].ttf"
  }
  files {
    source_file: "fonts/Funnel_Sans/variable/FunnelSans-Italic[wght].ttf"
    dest_file: "FunnelSans-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
stroke: "SANS_SERIF"
