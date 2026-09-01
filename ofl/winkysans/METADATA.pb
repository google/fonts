name: "Winky Sans"
designer: "Typofactur"
license: "OFL"
category: "SANS_SERIF"
date_added: "2025-02-21"
fonts {
  name: "Winky Sans"
  style: "normal"
  weight: 400
  filename: "WinkySans[wght].ttf"
  post_script_name: "WinkySans-Regular"
  full_name: "Winky Sans Regular"
  copyright: "Copyright 2024 The Winky Sans Project Authors (https://github.com/typofactur/winkysans.)"
}
fonts {
  name: "Winky Sans"
  style: "italic"
  weight: 400
  filename: "WinkySans-Italic[wght].ttf"
  post_script_name: "WinkySans-Italic"
  full_name: "Winky Sans Italic"
  copyright: "Copyright 2024 The Winky Sans Project Authors (https://github.com/typofactur/winkysans)"
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
  repository_url: "https://github.com/typofactur/winkysans"
  commit: "0c6c255d031c0328fcfcfbee5fbb87289ff18bc2"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/WinkySans[wght].ttf"
    dest_file: "WinkySans[wght].ttf"
  }
  files {
    source_file: "fonts/variable/WinkySans-Italic[wght].ttf"
    dest_file: "WinkySans-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
stroke: "SANS_SERIF"
classifications: "DISPLAY"
