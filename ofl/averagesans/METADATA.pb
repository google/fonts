name: "Average Sans"
designer: "Eduardo Tunni"
license: "OFL"
category: "SANS_SERIF"
date_added: "2012-10-26"
source {
  repository_url: "https://github.com/googlefonts/averagesans"
  commit: "1b1058cd63195d26fe2ccc70a7662d90220373ac"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/AverageSans-Regular.ttf"
    dest_file: "AverageSans-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}

fonts {
  name: "Average Sans"
  style: "normal"
  weight: 400
  filename: "AverageSans-Regular.ttf"
  post_script_name: "AverageSans-Regular"
  full_name: "Average Sans Regular"
  copyright: "Copyright (c) 2012, Eduardo Tunni (http://www.tipo.net.ar), with Reserved Font Name \'Average\'"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
