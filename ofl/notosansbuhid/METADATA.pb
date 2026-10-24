name: "Noto Sans Buhid"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Buhid"
  style: "normal"
  weight: 400
  filename: "NotoSansBuhid-Regular.ttf"
  post_script_name: "NotoSansBuhid-Regular"
  full_name: "Noto Sans Buhid Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/buhid)"
}
subsets: "buhid"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/buhid"
  commit: "f678808af467ed38aa5a8d29a3f0925c14b1f570"
  archive_url: "https://github.com/notofonts/buhid/releases/download/NotoSansBuhid-v2.001/NotoSansBuhid-v2.001.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansBuhid/full/ttf/NotoSansBuhid-Regular.ttf"
    dest_file: "NotoSansBuhid-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-buhid.yaml"
}
is_noto: true
languages: "bku_Buhd"
primary_script: "Buhd"
