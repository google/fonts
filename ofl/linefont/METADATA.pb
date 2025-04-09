name: "Linefont"
designer: "Dmitry Ivanov"
license: "OFL"
category: "DISPLAY"
date_added: "2023-09-27"
fonts {
  name: "Linefont"
  style: "normal"
  weight: 400
  filename: "Linefont[wdth,wght].ttf"
  post_script_name: "Linefont-Thin"
  full_name: "Linefont Thin"
  copyright: "Copyright 2022 The Linefont Project Authors (https://github.com/dy/linefont)"
}
subsets: "menu"
axes {
  tag: "wdth"
  min_value: 25.0
  max_value: 200.0
}
axes {
  tag: "wght"
  min_value: 4.0
  max_value: 1000.0
}
source {
  repository_url: "https://github.com/dy/linefont"
  commit: "9edec1a1f780db52db0297bab464451f3dbd4d5a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Linefont[wdth,wght].ttf"
    dest_file: "Linefont[wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
sample_text {
  masthead_full: "ĀŤĀŤĀŤĀŤĀŤĀŤĀŤŤĀĀŤŤĀĀŤŤĀĀŤŤĀĀŤŤĀĀŤŤŤŤĀĀĀĀŤŤŤŤĀĀĀĀŤŤŤŤĀĀ"
  masthead_partial: "ĀĀŤŤĀĀ"
  styles: "ĀŤĀŤĀŤĀŤĀŤĀŤĀŤŤĀĀŤŤĀĀŤŤĀĀŤŤĀĀŤŤĀĀŤŤŤŤĀĀĀĀŤŤŤŤĀĀĀĀŤŤŤŤĀĀŤŤŤŤĀĀĀĀŤŤŤŤŤŤŤŤĀĀĀĀĀĀĀĀŤŤŤŤŤŤŤŤĀĀĀĀ"
  tester: "ĀŤĀŤĀŤĀŤĀŤĀŤĀŤŤĀĀŤŤĀĀŤŤĀĀŤŤĀĀŤŤĀĀŤŤŤŤĀĀĀĀŤŤŤŤĀĀĀĀŤŤŤŤĀĀŤŤŤŤĀĀĀĀŤŤŤŤŤŤŤŤĀĀĀĀĀĀĀĀŤŤŤŤŤŤŤŤĀĀĀĀĀĀĀĀĀĀĀŤŤŤŤŤŤŤŤŤŤŤŤŤŤŤŤĀĀĀĀĀĀĀĀĀĀĀĀĀĀĀĀŤŤŤŤŤŤŤŤŤŤŤŤŤŤŤŤĀĀĀĀĀĀĀĀ"
}
minisite_url: "https://dy.github.io/linefont/scripts/"
classifications: "SYMBOLS"
classifications: "DISPLAY"
