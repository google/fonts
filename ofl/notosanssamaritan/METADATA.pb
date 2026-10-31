name: "Noto Sans Samaritan"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Samaritan"
  style: "normal"
  weight: 400
  filename: "NotoSansSamaritan-Regular.ttf"
  post_script_name: "NotoSansSamaritan-Regular"
  full_name: "Noto Sans Samaritan Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/samaritan)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "samaritan"
source {
  repository_url: "https://github.com/notofonts/samaritan"
  commit: "86c2e96b021b020d39b51641a541443e36c7ce62"
  archive_url: "https://github.com/notofonts/samaritan/releases/download/NotoSansSamaritan-v2.001/NotoSansSamaritan-v2.001.zip"
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
    source_file: "NotoSansSamaritan/googlefonts/ttf/NotoSansSamaritan-Regular.ttf"
    dest_file: "NotoSansSamaritan-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-samaritan.yaml"
}
is_noto: true
languages: "aii_Samr"
languages: "sam_Samr"
languages: "smp_Samr"
primary_script: "Samr"
