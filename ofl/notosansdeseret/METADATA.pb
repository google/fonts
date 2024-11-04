name: "Noto Sans Deseret"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Deseret"
  style: "normal"
  weight: 400
  filename: "NotoSansDeseret-Regular.ttf"
  post_script_name: "NotoSansDeseret-Regular"
  full_name: "Noto Sans Deseret Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/deseret)"
}
subsets: "deseret"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/deseret"
  archive_url: "https://github.com/notofonts/deseret/releases/download/NotoSansDeseret-v2.001/NotoSansDeseret-v2.001.zip"
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
    source_file: "NotoSansDeseret/googlefonts/ttf/NotoSansDeseret-Regular.ttf"
    dest_file: "NotoSansDeseret-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "en_Dsrt"  # English, Deseret
primary_script: "Dsrt"
