name: "Noto Sans Carian"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Carian"
  style: "normal"
  weight: 400
  filename: "NotoSansCarian-Regular.ttf"
  post_script_name: "NotoSansCarian-Regular"
  full_name: "Noto Sans Carian Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/carian)"
}
subsets: "carian"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/carian"
  archive_url: "https://github.com/notofonts/carian/releases/download/NotoSansCarian-v2.002/NotoSansCarian-v2.002.zip"
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSansCarian/googlefonts/ttf/NotoSansCarian-Regular.ttf"
    dest_file: "NotoSansCarian-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "xcr_Cari"  # Carian
primary_script: "Cari"
