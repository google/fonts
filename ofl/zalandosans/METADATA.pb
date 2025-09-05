name: "Zalando Sans"
designer: "Jakob Ekelund, KH Type, Zalando"
license: "OFL"
category: "SANS_SERIF"
date_added: "2025-07-14"
fonts {
  name: "Zalando Sans"
  style: "normal"
  weight: 400
  filename: "ZalandoSans[wdth,wght].ttf"
  post_script_name: "ZalandoSans-Regular"
  full_name: "Zalando Sans Regular"
  copyright: "Copyright 2025 The Zalando Sans Project Authors (https://github.com/zalando/sans)"
}
fonts {
  name: "Zalando Sans"
  style: "italic"
  weight: 400
  filename: "ZalandoSans-Italic[wdth,wght].ttf"
  post_script_name: "ZalandoSans-Italic"
  full_name: "Zalando Sans Italic"
  copyright: "Copyright 2025 The Zalando Sans Project Authors (https://github.com/zalando/sans)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wdth"
  min_value: 75.0
  max_value: 125.0
}
axes {
  tag: "wght"
  min_value: 200.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/zalando/sans"
  commit: "2fe06d0700b5b9ccd18a52c240e8927f48e92629"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/ZalandoSans[wdth,wght].ttf"
    dest_file: "ZalandoSans[wdth,wght].ttf"
  }
  files {
    source_file: "fonts/variable/ZalandoSans-Italic[wdth,wght].ttf"
    dest_file: "ZalandoSans-Italic[wdth,wght].ttf"
  }
  branch: "main"
}
stroke: "SANS_SERIF"
