name: "Fruktur"
designer: "Viktoriya Grabowska, Eben Sorkin"
license: "OFL"
category: "DISPLAY"
date_added: "2013-01-16"
fonts {
  name: "Fruktur"
  style: "normal"
  weight: 400
  filename: "Fruktur-Regular.ttf"
  post_script_name: "Fruktur-Regular"
  full_name: "Fruktur Regular"
  copyright: "Copyright 2022 The Fruktur Project Authors (https://github.com/SorkinType/Fruktur)"
}
fonts {
  name: "Fruktur"
  style: "italic"
  weight: 400
  filename: "Fruktur-Italic.ttf"
  post_script_name: "Fruktur-Italic"
  full_name: "Fruktur Italic"
  copyright: "Copyright 2022 The Fruktur Project Authors (https://github.com/SorkinType/Fruktur)"
}
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
source {
  repository_url: "https://github.com/SorkinType/Fruktur"
  commit: "0f8b79b91438420d4c158890cb28bcb1eef407a0"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Fruktur-Regular.ttf"
    dest_file: "Fruktur-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/Fruktur-Italic.ttf"
    dest_file: "Fruktur-Italic.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
