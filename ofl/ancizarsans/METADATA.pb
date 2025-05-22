name: "Ancizar Sans"
designer: "Universidad Nacional de Colombia (UNAL), César Puertas, Viviana Monsalve, Julián Moncada"
license: "OFL"
category: "SANS_SERIF"
date_added: "2025-04-16"
fonts {
  name: "Ancizar Sans"
  style: "normal"
  weight: 400
  filename: "AncizarSans[wght].ttf"
  post_script_name: "AncizarSans-Thin"
  full_name: "Ancizar Sans Thin"
  copyright: "Copyright 2014 The Ancizar Sans Project Authors (https://github.com/UNAL-OMD/UNAL-Ancizar)"
}
fonts {
  name: "Ancizar Sans"
  style: "italic"
  weight: 400
  filename: "AncizarSans-Italic[wght].ttf"
  post_script_name: "AncizarSans-ThinItalic"
  full_name: "Ancizar Sans Thin Italic"
  copyright: "Copyright 2014 The Ancizar Sans Project Authors (https://github.com/UNAL-OMD/UNAL-Ancizar)"
}
subsets: "greek"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 1000.0
}
source {
  repository_url: "https://github.com/UNAL-OMD/UNAL-Ancizar"
  commit: "54a5aa2153b4485ff2710612d47183c346e6b842"
  config_yaml: "sources/config-sans.yaml"
  files {
    source_file: "article/ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "article/specimen.jpg"
    dest_file: "article/specimen.jpg"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/AncizarSans[wght].ttf"
    dest_file: "AncizarSans[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AncizarSans-Italic[wght].ttf"
    dest_file: "AncizarSans-Italic[wght].ttf"
  }
  branch: "main"
}
