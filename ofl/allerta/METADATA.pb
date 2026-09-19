name: "Allerta"
designer: "Matt McInerney"
license: "OFL"
category: "SANS_SERIF"
date_added: "2010-11-30"
source {
  repository_url: "https://github.com/googlefonts/allerta"
  commit: "bdd9557493a2cdd003d2dcbc9a37d47868ec3606"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Allerta-Regular.ttf"
    dest_file: "Allerta-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}

fonts {
  name: "Allerta"
  style: "normal"
  weight: 400
  filename: "Allerta-Regular.ttf"
  post_script_name: "Allerta-Regular"
  full_name: "Allerta Regular"
  copyright: "Copyright (c) 2009, Matt McInerney <matt@pixelspread.com>"
}
subsets: "menu"
subsets: "latin"
