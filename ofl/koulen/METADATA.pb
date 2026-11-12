name: "Koulen"
designer: "Danh Hong"
license: "OFL"
category: "DISPLAY"
date_added: "2011-03-02"
fonts {
  name: "Koulen"
  style: "normal"
  weight: 400
  filename: "Koulen-Regular.ttf"
  post_script_name: "Koulen-Regular"
  full_name: "Koulen Regular"
  copyright: "Copyright 2019 The Koulen Project Authors (https://github.com/danhhong/Koulen)"
}
subsets: "khmer"
subsets: "latin"
subsets: "menu"
source {
  repository_url: "https://github.com/danhhong/Koulen"
  commit: "387ec6f230e61fe85a90529543daeeb2a3625b7e"
  config_yaml: "Source/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Release/ttf/Koulen-Regular.ttf"
    dest_file: "Koulen-Regular.ttf"
  }
  branch: "master"
}
primary_script: "Khmr"
stroke: "SANS_SERIF"
classifications: "DISPLAY"
