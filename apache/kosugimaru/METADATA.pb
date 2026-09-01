name: "Kosugi Maru"
designer: "MOTOYA"
license: "APACHE2"
category: "SANS_SERIF"
date_added: "2021-09-08"
fonts {
  name: "Kosugi Maru"
  style: "normal"
  weight: 400
  filename: "KosugiMaru-Regular.ttf"
  post_script_name: "KosugiMaru-Regular"
  full_name: "Kosugi Maru Regular"
  copyright: "Copyright 2010 The Kosugi Maru Project Authors (https://github.com/googlefonts/kosugi-maru)"
}
subsets: "cyrillic"
subsets: "japanese"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/googlefonts/kosugi-maru"
  commit: "bd22c671a9ffc10cc4313e6f2fd75f2b86d6b14b"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/ttf/KosugiMaru-Regular.ttf"
    dest_file: "KosugiMaru-Regular.ttf"
  }
  files {
    source_file: "LICENSE.txt"
    dest_file: "LICENSE.txt"
  }
  branch: "main"
}
primary_script: "Jpan"
