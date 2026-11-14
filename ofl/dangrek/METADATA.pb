name: "Dangrek"
designer: "Danh Hong"
license: "OFL"
category: "DISPLAY"
date_added: "2011-03-02"
fonts {
  name: "Dangrek"
  style: "normal"
  weight: 400
  filename: "Dangrek-Regular.ttf"
  post_script_name: "Dangrek-Regular"
  full_name: "Dangrek Regular"
  copyright: "Copyright 2020 The Dangrek Project Authors (https://github.com/danhhong/Dangrek)"
}
subsets: "khmer"
subsets: "latin"
subsets: "menu"
source {
  repository_url: "https://github.com/danhhong/Dangrek"
  commit: "a8da8cf02ec7e96f45716b0052a027007bb042c2"
  config_yaml: "Source/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Release/ttf/Dangrek-Regular.ttf"
    dest_file: "Dangrek-Regular.ttf"
  }
  branch: "master"
}
primary_script: "Khmr"
stroke: "SANS_SERIF"
classifications: "DISPLAY"
