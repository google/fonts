name: "DM Sans"
designer: "Colophon Foundry"
license: "OFL"
category: "SANS_SERIF"
date_added: "2019-06-12"
fonts {
  name: "DM Sans"
  style: "normal"
  weight: 400
  filename: "DMSans[opsz,wght].ttf"
  post_script_name: "DMSans-9ptRegular"
  full_name: "DM Sans 9pt Regular"
  copyright: "Copyright 2014 The DM Sans Project Authors (https://github.com/googlefonts/dm-fonts)"
}
fonts {
  name: "DM Sans"
  style: "italic"
  weight: 400
  filename: "DMSans-Italic[opsz,wght].ttf"
  post_script_name: "DMSans-9ptItalic"
  full_name: "DM Sans 9pt Italic"
  copyright: "Copyright 2014 The DM Sans Project Authors (https://github.com/googlefonts/dm-fonts)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "opsz"
  min_value: 9.0
  max_value: 40.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 1000.0
}
source {
  repository_url: "https://github.com/googlefonts/dm-fonts"
  commit: "d0520ba03bd780f5dccb3024854463d44f699b78"
  files {
    source_file: "Sans/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Sans/fonts/variable/DMSans[opsz,wght].ttf"
    dest_file: "DMSans[opsz,wght].ttf"
  }
  files {
    source_file: "Sans/fonts/variable/DMSans-Italic[opsz,wght].ttf"
    dest_file: "DMSans-Italic[opsz,wght].ttf"
  }
  branch: "main"
}
