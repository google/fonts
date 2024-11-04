name: "Noto Sans Coptic"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Coptic"
  style: "normal"
  weight: 400
  filename: "NotoSansCoptic-Regular.ttf"
  post_script_name: "NotoSansCoptic-Regular"
  full_name: "Noto Sans Coptic Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/coptic)"
}
subsets: "coptic"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/coptic"
  archive_url: "https://github.com/notofonts/coptic/releases/download/NotoSansCoptic-v2.004/NotoSansCoptic-v2.004.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "NotoSansCoptic/googlefonts/ttf/NotoSansCoptic-Regular.ttf"
    dest_file: "NotoSansCoptic-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "cop_Copt"  # Coptic, Coptic
primary_script: "Copt"
