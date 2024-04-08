name: "Noto Sans Marchen"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Marchen"
  style: "normal"
  weight: 400
  filename: "NotoSansMarchen-Regular.ttf"
  post_script_name: "NotoSansMarchen-Regular"
  full_name: "Noto Sans Marchen Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/marchen)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "marchen"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/marchen"
  archive_url: "https://github.com/notofonts/marchen/releases/download/NotoSansMarchen-v2.003/NotoSansMarchen-v2.003.zip"
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
    source_file: "NotoSansMarchen/googlefonts/ttf/NotoSansMarchen-Regular.ttf"
    dest_file: "NotoSansMarchen-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "bo_Marc"  # Tibetan, Marchen
languages: "sa_Marc"  # Sanskrit, Marchen
primary_script: "Marc"
