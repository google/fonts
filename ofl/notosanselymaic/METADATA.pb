name: "Noto Sans Elymaic"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Elymaic"
  style: "normal"
  weight: 400
  filename: "NotoSansElymaic-Regular.ttf"
  post_script_name: "NotoSansElymaic-Regular"
  full_name: "Noto Sans Elymaic Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/elymaic)"
}
subsets: "elymaic"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/elymaic"
  archive_url: "https://github.com/notofonts/elymaic/releases/download/NotoSansElymaic-v1.002/NotoSansElymaic-v1.002.zip"
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
    source_file: "NotoSansElymaic/googlefonts/ttf/NotoSansElymaic-Regular.ttf"
    dest_file: "NotoSansElymaic-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "aii_Elym"  # Assyrian Neo-Aramaic, Elymaic
languages: "xly_Elym"  # Elymian
