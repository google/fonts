name: "Ledger"
designer: "Denis Masharov"
license: "OFL"
category: "SERIF"
date_added: "2012-02-22"
fonts {
  name: "Ledger"
  style: "normal"
  weight: 400
  filename: "Ledger-Regular.ttf"
  post_script_name: "Ledger-Regular"
  full_name: "Ledger"
  copyright: "Copyright (c) 2011, Denis Masharov <denis.masharov@gmail.com>."
}
subsets: "menu"
subsets: "cyrillic"
subsets: "latin"
subsets: "latin-ext"
source {
  repository_url: "https://github.com/googlefonts/ledger"
  commit: "35047d53a9fc5fb41e185e1f4c4a9532eca001b1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Ledger-Regular.ttf"
    dest_file: "Ledger-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
