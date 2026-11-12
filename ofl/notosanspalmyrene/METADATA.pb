name: "Noto Sans Palmyrene"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Palmyrene"
  style: "normal"
  weight: 400
  filename: "NotoSansPalmyrene-Regular.ttf"
  post_script_name: "NotoSansPalmyrene-Regular"
  full_name: "Noto Sans Palmyrene Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/palmyrene)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "palmyrene"
source {
  repository_url: "https://github.com/notofonts/palmyrene"
  commit: "bbb69ea150a25cabb937bcbd654c171ff958b426"
  archive_url: "https://github.com/notofonts/palmyrene/releases/download/NotoSansPalmyrene-v2.001/NotoSansPalmyrene-v2.001.zip"
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
    source_file: "NotoSansPalmyrene/googlefonts/ttf/NotoSansPalmyrene-Regular.ttf"
    dest_file: "NotoSansPalmyrene-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-palmyrene.yaml"
}
is_noto: true
languages: "aii_Palm"
languages: "arc_Palm"
primary_script: "Palm"
