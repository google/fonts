name: "Bitter"
designer: "Sol Matas"
license: "OFL"
category: "SERIF"
date_added: "2011-12-19"
fonts {
  name: "Bitter"
  style: "normal"
  weight: 400
  filename: "Bitter[wght].ttf"
  post_script_name: "Bitter-Thin"
  full_name: "Bitter Thin"
  copyright: "Copyright 2011 The Bitter Project Authors (https://github.com/solmatas/BitterPro)"
}
fonts {
  name: "Bitter"
  style: "italic"
  weight: 400
  filename: "Bitter-Italic[wght].ttf"
  post_script_name: "Bitter-ThinItalic"
  full_name: "Bitter Thin Italic"
  copyright: "Copyright 2011 The Bitter Project Authors (https://github.com/solmatas/BitterPro)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
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
  repository_url: "https://github.com/solmatas/BitterPro"
  commit: "3238d7ae2cb0b564b81225d68b3c893a40b1d3ce"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Bitter[wght].ttf"
    dest_file: "Bitter[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Bitter-Italic[wght].ttf"
    dest_file: "Bitter-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
