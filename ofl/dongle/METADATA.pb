name: "Dongle"
designer: "Yanghee Ryu"
license: "OFL"
category: "SANS_SERIF"
date_added: "2021-06-14"
fonts {
  name: "Dongle"
  style: "normal"
  weight: 300
  filename: "Dongle-Light.ttf"
  post_script_name: "Dongle-Light"
  full_name: "Dongle Light"
  copyright: "Copyright 2021 The Dongle Project Authors (https://github.com/yangheeryu/Dongle)"
}
fonts {
  name: "Dongle"
  style: "normal"
  weight: 400
  filename: "Dongle-Regular.ttf"
  post_script_name: "Dongle-Regular"
  full_name: "Dongle Regular"
  copyright: "Copyright 2021 The Dongle Project Authors (https://github.com/yangheeryu/Dongle)"
}
fonts {
  name: "Dongle"
  style: "normal"
  weight: 700
  filename: "Dongle-Bold.ttf"
  post_script_name: "Dongle-Bold"
  full_name: "Dongle Bold"
  copyright: "Copyright 2021 The Dongle Project Authors (https://github.com/yangheeryu/Dongle)"
}
subsets: "korean"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
source {
  repository_url: "https://github.com/googlefonts/dongle"
  commit: "d424e1283eec663ccc1cc66c8ea7f7262d7a8b04"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Dongle-Bold.ttf"
    dest_file: "Dongle-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Dongle-Light.ttf"
    dest_file: "Dongle-Light.ttf"
  }
  files {
    source_file: "fonts/ttf/Dongle-Regular.ttf"
    dest_file: "Dongle-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
primary_script: "Kore"
stroke: "SANS_SERIF"
classifications: "DISPLAY"
