name: "Noto Sans Buginese"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Buginese"
  style: "normal"
  weight: 400
  filename: "NotoSansBuginese-Regular.ttf"
  post_script_name: "NotoSansBuginese-Regular"
  full_name: "Noto Sans Buginese Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/buginese)"
}
subsets: "buginese"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/buginese"
  archive_url: "https://github.com/notofonts/buginese/releases/download/NotoSansBuginese-v2.002/NotoSansBuginese-v2.002.zip"
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
    source_file: "NotoSansBuginese/googlefonts/ttf/NotoSansBuginese-Regular.ttf"
    dest_file: "NotoSansBuginese-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "bug_Bugi"  # Buginese, Buginese
languages: "mak_Bugi"  # Makasar, Buginese
languages: "mdr_Bugi"  # Mandar, Buginese
languages: "sa_Bugi"  # Sanskrit, Buginese
primary_script: "Bugi"
