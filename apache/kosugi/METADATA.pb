name: "Kosugi"
designer: "MOTOYA"
license: "APACHE2"
category: "SANS_SERIF"
date_added: "2021-09-08"
fonts {
  name: "Kosugi"
  style: "normal"
  weight: 400
  filename: "Kosugi-Regular.ttf"
  post_script_name: "Kosugi-Regular"
  full_name: "Kosugi Regular"
  copyright: "Copyright 2010 The Kosugi Project Authors (https://github.com/googlefonts/kosugi)"
}
subsets: "cyrillic"
subsets: "japanese"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/googlefonts/kosugi"
  commit: "75171a2738135ab888549e76a9037e826094f0ce"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/ttf/Kosugi-Regular.ttf"
    dest_file: "Kosugi-Regular.ttf"
  }
  files {
    source_file: "LICENSE.txt"
    dest_file: "LICENSE.txt"
  }
  branch: "main"
}
primary_script: "Jpan"
