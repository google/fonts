name: "Azeret Mono"
designer: "Displaay, Martin Vácha"
license: "OFL"
category: "MONOSPACE"
date_added: "2021-06-08"
fonts {
  name: "Azeret Mono"
  style: "normal"
  weight: 400
  filename: "AzeretMono[wght].ttf"
  post_script_name: "AzeretMono-Thin"
  full_name: "Azeret Mono Thin"
  copyright: "Copyright 2021 The Azeret Project Authors (https://github.com/displaay/azeret)"
}
fonts {
  name: "Azeret Mono"
  style: "italic"
  weight: 400
  filename: "AzeretMono-Italic[wght].ttf"
  post_script_name: "AzeretMono-ThinItalic"
  full_name: "Azeret Mono Thin Italic"
  copyright: "Copyright 2021 The Azeret Project Authors (https://github.com/displaay/azeret)"
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
  repository_url: "https://github.com/displaay/Azeret"
  files {
    source_file: "fonts/variable/AzeretMono[wght].ttf"
    dest_file: "AzeretMono[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AzeretMono-Italic[wght].ttf"
    dest_file: "AzeretMono-Italic[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
}
