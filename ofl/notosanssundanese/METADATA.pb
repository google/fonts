name: "Noto Sans Sundanese"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Sundanese"
  style: "normal"
  weight: 400
  filename: "NotoSansSundanese[wght].ttf"
  post_script_name: "NotoSansSundanese-Regular"
  full_name: "Noto Sans Sundanese Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/sundanese)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "sundanese"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/notofonts/sundanese"
  archive_url: "https://github.com/notofonts/sundanese/releases/download/NotoSansSundanese-v2.005/NotoSansSundanese-v2.005.zip"
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
    source_file: "NotoSansSundanese/googlefonts/variable/NotoSansSundanese[wght].ttf"
    dest_file: "NotoSansSundanese[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "sa_Sund"  # Sanskrit, Sundanese
languages: "su_Sund"  # Sundanese, Sundanese
primary_script: "Sund"
