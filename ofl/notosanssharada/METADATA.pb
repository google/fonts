name: "Noto Sans Sharada"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Sharada"
  style: "normal"
  weight: 400
  filename: "NotoSansSharada-Regular.ttf"
  post_script_name: "NotoSansSharada-Regular"
  full_name: "Noto Sans Sharada Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/sharada)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "sharada"
source {
  repository_url: "https://github.com/notofonts/sharada"
  archive_url: "https://github.com/notofonts/sharada/releases/download/NotoSansSharada-v2.006/NotoSansSharada-v2.006.zip"
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansSharada/googlefonts/ttf/NotoSansSharada-Regular.ttf"
    dest_file: "NotoSansSharada-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "sa_Shrd"  # Sanskrit, Sharada
primary_script: "Shrd"
