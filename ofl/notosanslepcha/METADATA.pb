name: "Noto Sans Lepcha"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Lepcha"
  style: "normal"
  weight: 400
  filename: "NotoSansLepcha-Regular.ttf"
  post_script_name: "NotoSansLepcha-Regular"
  full_name: "Noto Sans Lepcha Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/lepcha)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "lepcha"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/lepcha"
  commit: "22993dbe4ed924277e75a444a40d2b420a372e7c"
  archive_url: "https://github.com/notofonts/lepcha/releases/download/NotoSansLepcha-v2.006/NotoSansLepcha-v2.006.zip"
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
    source_file: "NotoSansLepcha/googlefonts/ttf/NotoSansLepcha-Regular.ttf"
    dest_file: "NotoSansLepcha-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-lepcha.yaml"
}
is_noto: true
languages: "lep_Lepc"
primary_script: "Lepc"
