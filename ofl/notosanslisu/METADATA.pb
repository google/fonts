name: "Noto Sans Lisu"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Lisu"
  style: "normal"
  weight: 400
  filename: "NotoSansLisu[wght].ttf"
  post_script_name: "NotoSansLisu-Regular"
  full_name: "Noto Sans Lisu Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/lisu)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "lisu"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/notofonts/lisu"
  commit: "d7e34571c41408f05975acaee719c2353408eb9e"
  archive_url: "https://github.com/notofonts/lisu/releases/download/NotoSansLisu-v2.102/NotoSansLisu-v2.102.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansLisu/googlefonts/variable-ttf/NotoSansLisu[wght].ttf"
    dest_file: "NotoSansLisu[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-lisu.yaml"
}
is_noto: true
languages: "lis_Lisu"
primary_script: "Lisu"
