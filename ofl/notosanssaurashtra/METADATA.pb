name: "Noto Sans Saurashtra"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Saurashtra"
  style: "normal"
  weight: 400
  filename: "NotoSansSaurashtra-Regular.ttf"
  post_script_name: "NotoSansSaurashtra-Regular"
  full_name: "Noto Sans Saurashtra Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/saurashtra)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "saurashtra"
source {
  repository_url: "https://github.com/notofonts/saurashtra"
  archive_url: "https://github.com/notofonts/saurashtra/releases/download/NotoSansSaurashtra-v2.002/NotoSansSaurashtra-v2.002.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansSaurashtra/googlefonts/ttf/NotoSansSaurashtra-Regular.ttf"
    dest_file: "NotoSansSaurashtra-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "saz_Saur"  # Saurashtra
primary_script: "Saur"
