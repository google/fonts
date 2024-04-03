name: "Noto Sans Batak"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Batak"
  style: "normal"
  weight: 400
  filename: "NotoSansBatak-Regular.ttf"
  post_script_name: "NotoSansBatak-Regular"
  full_name: "Noto Sans Batak Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/batak)"
}
subsets: "batak"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/batak"
  archive_url: "https://github.com/notofonts/batak/releases/download/NotoSansBatak-v2.003/NotoSansBatak-v2.003.zip"
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
    source_file: "NotoSansBatak/googlefonts/ttf/NotoSansBatak-Regular.ttf"
    dest_file: "NotoSansBatak-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "bbc_Batk"  # Batak Toba, Batak
primary_script: "Batk"
