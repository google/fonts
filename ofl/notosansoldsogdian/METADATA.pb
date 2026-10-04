name: "Noto Sans Old Sogdian"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Old Sogdian"
  style: "normal"
  weight: 400
  filename: "NotoSansOldSogdian-Regular.ttf"
  post_script_name: "NotoSansOldSogdian-Regular"
  full_name: "Noto Sans Old Sogdian Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/old-sogdian)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "old-sogdian"
source {
  repository_url: "https://github.com/notofonts/old-sogdian"
  commit: "aa13b986b6b48a97ab305a8915d2349fdfc87692"
  archive_url: "https://github.com/notofonts/old-sogdian/releases/download/NotoSansOldSogdian-v2.003/NotoSansOldSogdian-v2.003.zip"
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
    source_file: "NotoSansOldSogdian/googlefonts/ttf/NotoSansOldSogdian-Regular.ttf"
    dest_file: "NotoSansOldSogdian-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-old-sogdian.yaml"
}
is_noto: true
languages: "aii_Sogo"
languages: "sog_Sogo"
primary_script: "Sogo"
