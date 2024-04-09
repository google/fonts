name: "Noto Sans Tagalog"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Tagalog"
  style: "normal"
  weight: 400
  filename: "NotoSansTagalog-Regular.ttf"
  post_script_name: "NotoSansTagalog-Regular"
  full_name: "Noto Sans Tagalog Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/tagalog)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "tagalog"
source {
  repository_url: "https://github.com/notofonts/tagalog"
  archive_url: "https://github.com/notofonts/tagalog/releases/download/NotoSansTagalog-v2.002/NotoSansTagalog-v2.002.zip"
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSansTagalog/googlefonts/ttf/NotoSansTagalog-Regular.ttf"
    dest_file: "NotoSansTagalog-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "fil_Tglg"  # Filipino, Tagalog
primary_script: "Tglg"
