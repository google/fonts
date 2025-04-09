name: "Noto Sans Miao"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Miao"
  style: "normal"
  weight: 400
  filename: "NotoSansMiao-Regular.ttf"
  post_script_name: "NotoSansMiao-Regular"
  full_name: "Noto Sans Miao Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/miao)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "miao"
source {
  repository_url: "https://github.com/notofonts/miao"
  commit: "60e05da3a76e726c5496c3dcbead5051e8b782f7"
  archive_url: "https://github.com/notofonts/miao/releases/download/NotoSansMiao-v2.003/NotoSansMiao-v2.003.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSansMiao/googlefonts/ttf/NotoSansMiao-Regular.ttf"
    dest_file: "NotoSansMiao-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-miao.yaml"
}
is_noto: true
languages: "hmd_Plrd"
primary_script: "Plrd"
