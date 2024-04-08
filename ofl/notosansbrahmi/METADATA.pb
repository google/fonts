name: "Noto Sans Brahmi"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Brahmi"
  style: "normal"
  weight: 400
  filename: "NotoSansBrahmi-Regular.ttf"
  post_script_name: "NotoSansBrahmi-Regular"
  full_name: "Noto Sans Brahmi Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/brahmi)"
}
subsets: "brahmi"
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "symbols"
source {
  repository_url: "https://github.com/notofonts/brahmi"
  archive_url: "https://github.com/notofonts/brahmi/releases/download/NotoSansBrahmi-v2.004/NotoSansBrahmi-v2.004.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "NotoSansBrahmi/googlefonts/ttf/NotoSansBrahmi-Regular.ttf"
    dest_file: "NotoSansBrahmi-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "aii_Brah"  # Assyrian Neo-Aramaic, Brahmi
languages: "pi_Brah"  # Pali, Brahmi
languages: "pka_Brah"  # Ardhamagadhi Prakrit
languages: "sa_Brah"  # Sanskrit, Brahmi
primary_script: "Brah"
