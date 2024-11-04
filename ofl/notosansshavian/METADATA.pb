name: "Noto Sans Shavian"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Shavian"
  style: "normal"
  weight: 400
  filename: "NotoSansShavian-Regular.ttf"
  post_script_name: "NotoSansShavian-Regular"
  full_name: "Noto Sans Shavian Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/shavian)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "shavian"
source {
  repository_url: "https://github.com/notofonts/shavian"
  archive_url: "https://github.com/notofonts/shavian/releases/download/NotoSansShavian-v2.001/NotoSansShavian-v2.001.zip"
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
    source_file: "NotoSansShavian/googlefonts/ttf/NotoSansShavian-Regular.ttf"
    dest_file: "NotoSansShavian-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "en_Shaw"  # English, Shavian
primary_script: "Shaw"
