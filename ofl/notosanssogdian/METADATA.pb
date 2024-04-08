name: "Noto Sans Sogdian"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Sogdian"
  style: "normal"
  weight: 400
  filename: "NotoSansSogdian-Regular.ttf"
  post_script_name: "NotoSansSogdian-Regular"
  full_name: "Noto Sans Sogdian Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/sogdian)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "sogdian"
source {
  repository_url: "https://github.com/notofonts/sogdian"
  archive_url: "https://github.com/notofonts/sogdian/releases/download/NotoSansSogdian-v2.002/NotoSansSogdian-v2.002.zip"
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
    source_file: "NotoSansSogdian/googlefonts/ttf/NotoSansSogdian-Regular.ttf"
    dest_file: "NotoSansSogdian-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "aii_Sogd"  # Assyrian Neo-Aramaic, Sogdian
languages: "sog_Sogd"  # Sogdian
primary_script: "Sogd"
