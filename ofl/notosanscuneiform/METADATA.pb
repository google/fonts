name: "Noto Sans Cuneiform"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Cuneiform"
  style: "normal"
  weight: 400
  filename: "NotoSansCuneiform-Regular.ttf"
  post_script_name: "NotoSansCuneiform-Regular"
  full_name: "Noto Sans Cuneiform Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/cuneiform)"
}
subsets: "cuneiform"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/cuneiform"
  archive_url: "https://github.com/notofonts/cuneiform/releases/download/NotoSansCuneiform-v2.001/NotoSansCuneiform-v2.001.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSansCuneiform/googlefonts/ttf/NotoSansCuneiform-Regular.ttf"
    dest_file: "NotoSansCuneiform-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "akk_Xsux"  # Akkadian
languages: "hit_Xsux"  # Hittite
primary_script: "Xsux"
