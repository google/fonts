name: "Roboto Mono"
designer: "Christian Robertson"
license: "APACHE2"
category: "MONOSPACE"
date_added: "2015-05-13"
fonts {
  name: "Roboto Mono"
  style: "normal"
  weight: 400
  filename: "RobotoMono[wght].ttf"
  post_script_name: "RobotoMono-Regular"
  full_name: "Roboto Mono Regular"
  copyright: "Copyright 2015 The Roboto Mono Project Authors (https://github.com/googlefonts/robotomono)"
}
fonts {
  name: "Roboto Mono"
  style: "italic"
  weight: 400
  filename: "RobotoMono-Italic[wght].ttf"
  post_script_name: "RobotoMono-Italic"
  full_name: "Roboto Mono Italic"
  copyright: "Copyright 2015 The Roboto Mono Project Authors (https://github.com/googlefonts/robotomono)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "greek"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/googlefonts/RobotoMono"
  commit: "111eb14e367888c9374da4da0b018e72cf8ac46d"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/variable/RobotoMono[wght].ttf"
    dest_file: "RobotoMono[wght].ttf"
  }
  files {
    source_file: "fonts/variable/RobotoMono-Italic[wght].ttf"
    dest_file: "RobotoMono-Italic[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
}
