name: "Noto Sans Multani"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Multani"
  style: "normal"
  weight: 400
  filename: "NotoSansMultani-Regular.ttf"
  post_script_name: "NotoSansMultani-Regular"
  full_name: "Noto Sans Multani Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/multani)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "multani"
source {
  repository_url: "https://github.com/notofonts/multani"
  archive_url: "https://github.com/notofonts/multani/releases/download/NotoSansMultani-v2.002/NotoSansMultani-v2.002.zip"
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
    source_file: "NotoSansMultani/googlefonts/ttf/NotoSansMultani-Regular.ttf"
    dest_file: "NotoSansMultani-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "sa_Mult"  # Sanskrit, Multani
languages: "skr_Mult"  # Saraiki, Multani
primary_script: "Mult"
