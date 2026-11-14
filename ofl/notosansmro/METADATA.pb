name: "Noto Sans Mro"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Mro"
  style: "normal"
  weight: 400
  filename: "NotoSansMro-Regular.ttf"
  post_script_name: "NotoSansMro-Regular"
  full_name: "Noto Sans Mro Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/mro)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "mro"
source {
  repository_url: "https://github.com/notofonts/mro"
  commit: "3d7debf9b0faf7750c1c9191e9bc348c2a1fcedd"
  archive_url: "https://github.com/notofonts/mro/releases/download/NotoSansMro-v2.001/NotoSansMro-v2.001.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSansMro/googlefonts/ttf/NotoSansMro-Regular.ttf"
    dest_file: "NotoSansMro-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-mro.yaml"
}
is_noto: true
languages: "mro_Mroo"
languages: "sa_Mroo"
primary_script: "Mroo"
