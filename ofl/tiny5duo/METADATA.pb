name: "Tiny5 Duo"
designer: "Stefan Schmidt"
license: "OFL"
category: "DISPLAY"
date_added: "2026-09-03"
fonts {
  name: "Tiny5 Duo"
  style: "normal"
  weight: 400
  filename: "Tiny5Duo[BLED,JITT,ROND,wdth,wght].ttf"
  post_script_name: "Tiny5Duo-Regular"
  full_name: "Tiny5 Duo Regular"
  copyright: "Copyright 2026 The Tiny5 Project Authors (https://github.com/Gissio/font_Tiny5)"
}
fonts {
  name: "Tiny5 Duo"
  style: "italic"
  weight: 400
  filename: "Tiny5Duo-Italic[BLED,JITT,ROND,wdth,wght].ttf"
  post_script_name: "Tiny5Duo-Italic"
  full_name: "Tiny5 Duo Italic"
  copyright: "Copyright 2026 The Tiny5 Project Authors (https://github.com/Gissio/font_Tiny5)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "greek"
subsets: "greek-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "BLED"
  min_value: 0.0
  max_value: 100.0
}
axes {
  tag: "JITT"
  min_value: 0.0
  max_value: 100.0
}
axes {
  tag: "ROND"
  min_value: 0.0
  max_value: 100.0
}
axes {
  tag: "wdth"
  min_value: 50.0
  max_value: 150.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/Gissio/font_tiny5"
  commit: "cd350d50285f80abb885160e5054353d02397129"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/ARTICLE.en_us.html"
    dest_file: "ARTICLE.en_us.html"
  }
  files {
    source_file: "fonts/variable/Tiny5Duo[BLED,JITT,ROND,wdth,wght].ttf"
    dest_file: "Tiny5Duo[BLED,JITT,ROND,wdth,wght].ttf"
  }
  files {
    source_file: "fonts/variable/Tiny5Duo-Italic[BLED,JITT,ROND,wdth,wght].ttf"
    dest_file: "Tiny5Duo-Italic[BLED,JITT,ROND,wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
stroke: "SANS_SERIF"
classifications: "DISPLAY"
