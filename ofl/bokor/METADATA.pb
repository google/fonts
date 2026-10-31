name: "Bokor"
designer: "Danh Hong"
license: "OFL"
category: "DISPLAY"
date_added: "2011-03-02"
fonts {
  name: "Bokor"
  style: "normal"
  weight: 400
  filename: "Bokor-Regular.ttf"
  post_script_name: "Bokor-Regular"
  full_name: "Bokor Regular"
  copyright: "Copyright 2020 The Bokor Project Authors (https://github.com/danhhong/Bokor)"
}
subsets: "khmer"
subsets: "latin"
subsets: "menu"
source {
  repository_url: "https://github.com/danhhong/Bokor"
  commit: "b5d5f6e07e365610ad5a39d42f87505e85702432"
  config_yaml: "Source/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Release/ttf/Bokor-Regular.ttf"
    dest_file: "Bokor-Regular.ttf"
  }
  branch: "master"
}
primary_script: "Khmr"
