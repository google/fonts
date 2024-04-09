name: "Noto Sans Gothic"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Gothic"
  style: "normal"
  weight: 400
  filename: "NotoSansGothic-Regular.ttf"
  post_script_name: "NotoSansGothic-Regular"
  full_name: "Noto Sans Gothic Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/gothic)"
}
subsets: "gothic"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/gothic"
  archive_url: "https://github.com/notofonts/gothic/releases/download/NotoSansGothic-v2.001/NotoSansGothic-v2.001.zip"
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
    source_file: "NotoSansGothic/googlefonts/ttf/NotoSansGothic-Regular.ttf"
    dest_file: "NotoSansGothic-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "got_Goth"  # Gothic
primary_script: "Goth"
