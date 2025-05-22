name: "Nokora"
designer: "Danh Hong"
license: "OFL"
category: "SANS_SERIF"
date_added: "2011-11-09"
fonts {
  name: "Nokora"
  style: "normal"
  weight: 400
  filename: "Nokora[wght].ttf"
  post_script_name: "Nokora-Regular"
  full_name: "Nokora Regular"
  copyright: "Copyright 2019 The Nokora Project Authors (https://github.com/danhhong/Nokora)"
}
subsets: "khmer"
subsets: "latin"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/danhhong/Nokora"
  commit: "9c5f991b700b9be3519315a854a7b986e6877ace"
  config_yaml: "Source/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Release/variable/Nokora[wght].ttf"
    dest_file: "Nokora[wght].ttf"
  }
  branch: "master"
}
primary_script: "Khmr"
