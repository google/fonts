name: "Radio Canada"
designer: "Charles Daoud, Coppers and Brasses, Alexandre Saumier Demers, Jacques Le Bailly"
license: "OFL"
category: "SANS_SERIF"
date_added: "2022-03-18"
fonts {
  name: "Radio Canada"
  style: "normal"
  weight: 400
  filename: "RadioCanada[wdth,wght].ttf"
  post_script_name: "RadioCanada-Regular"
  full_name: "Radio Canada Regular"
  copyright: "Copyright 2017 The Radio-Canada Project Authors (https://github.com/cbcrc/radiocanadafonts)"
}
fonts {
  name: "Radio Canada"
  style: "italic"
  weight: 400
  filename: "RadioCanada-Italic[wdth,wght].ttf"
  post_script_name: "RadioCanada-Italic"
  full_name: "Radio Canada Italic"
  copyright: "Copyright 2017 The Radio-Canada Project Authors (https://github.com/cbcrc/radiocanadafonts)"
}
subsets: "canadian-aboriginal"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wdth"
  min_value: 75.0
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/cbcrc/radiocanadafonts"
  commit: "61a4efa847d6361be8e9cd3c656b3256b29d4ff4"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/RadioCanada[wdth,wght].ttf"
    dest_file: "RadioCanada[wdth,wght].ttf"
  }
  files {
    source_file: "fonts/variable/RadioCanada-Italic[wdth,wght].ttf"
    dest_file: "RadioCanada-Italic[wdth,wght].ttf"
  }
  branch: "main"
}
