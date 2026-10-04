name: "Noto Sans Tifinagh"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Tifinagh"
  style: "normal"
  weight: 400
  filename: "NotoSansTifinagh-Regular.ttf"
  post_script_name: "NotoSansTifinagh-Regular"
  full_name: "Noto Sans Tifinagh Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/tifinagh)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "tifinagh"
source {
  repository_url: "https://github.com/notofonts/tifinagh"
  commit: "6c19a68ff330ec938fb21d6be8c94b2183e1b077"
  archive_url: "https://github.com/notofonts/tifinagh/releases/download/NotoSansTifinagh-v2.006/NotoSansTifinagh-v2.006.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "NotoSansTifinagh/googlefonts/ttf/NotoSansTifinagh-Regular.ttf"
    dest_file: "NotoSansTifinagh-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-tifinagh.yaml"
}
is_noto: true
languages: "ber_Tfng"
languages: "kab_Tfng"
languages: "rif_Tfng"
languages: "shi_Tfng"
languages: "taq_Tfng"
languages: "tzm_Tfng"
languages: "zen_Tfng"
languages: "zgh_Tfng"
primary_script: "Tfng"
