name: "Noto Sans Mahajani"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Mahajani"
  style: "normal"
  weight: 400
  filename: "NotoSansMahajani-Regular.ttf"
  post_script_name: "NotoSansMahajani-Regular"
  full_name: "Noto Sans Mahajani Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/mahajani)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "mahajani"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/mahajani"
  commit: "6af195b21b1841f6b842af2a3d2f6b252718a70d"
  archive_url: "https://github.com/notofonts/mahajani/releases/download/NotoSansMahajani-v2.003/NotoSansMahajani-v2.003.zip"
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
    source_file: "NotoSansMahajani/googlefonts/ttf/NotoSansMahajani-Regular.ttf"
    dest_file: "NotoSansMahajani-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-mahajani.yaml"
}
is_noto: true
languages: "hi_Mahj"
primary_script: "Mahj"
