name: "Coustard"
designer: "Vernon Adams"
license: "OFL"
category: "SERIF"
date_added: "2011-08-10"
fonts {
  name: "Coustard"
  style: "normal"
  weight: 400
  filename: "Coustard-Regular.ttf"
  post_script_name: "Coustard-Regular"
  full_name: "Coustard Regular"
  copyright: "Copyright 2011 The Coustard Project Authors (https://github.com/googlefonts/coustardFont)"
}
fonts {
  name: "Coustard"
  style: "normal"
  weight: 900
  filename: "Coustard-Black.ttf"
  post_script_name: "Coustard-Black"
  full_name: "Coustard Black"
  copyright: "Copyright 2011 The Coustard Project Authors (https://github.com/googlefonts/coustardFont)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/googlefonts/coustardFont"
  commit: "84d4ef2fbb8e87ba843d49308b98eeb4a874be91"
  files {
    source_file: "fonts/ttf/Coustard-Regular.ttf"
    dest_file: "Coustard-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/Coustard-Black.ttf"
    dest_file: "Coustard-Black.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
