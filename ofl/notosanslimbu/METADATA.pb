name: "Noto Sans Limbu"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Limbu"
  style: "normal"
  weight: 400
  filename: "NotoSansLimbu-Regular.ttf"
  post_script_name: "NotoSansLimbu-Regular"
  full_name: "Noto Sans Limbu Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/limbu)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "limbu"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/limbu"
  commit: "191ac5f51c1dc7603d7636a26161ff9c36b9671b"
  archive_url: "https://github.com/notofonts/limbu/releases/download/NotoSansLimbu-v2.005/NotoSansLimbu-v2.005.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansLimbu/googlefonts/ttf/NotoSansLimbu-Regular.ttf"
    dest_file: "NotoSansLimbu-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-limbu.yaml"
}
is_noto: true
languages: "lif_Limb"
primary_script: "Limb"
