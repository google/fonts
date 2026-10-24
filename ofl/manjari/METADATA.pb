name: "Manjari"
designer: "Santhosh Thottingal"
license: "OFL"
category: "SANS_SERIF"
date_added: "2018-11-21"
fonts {
  name: "Manjari"
  style: "normal"
  weight: 100
  filename: "Manjari-Thin.ttf"
  post_script_name: "Manjari-Thin"
  full_name: "Manjari Thin"
  copyright: "Copyright 2018 The Manjari Project Authors (https://gitlab.com/smc/fonts/manjari)"
}
fonts {
  name: "Manjari"
  style: "normal"
  weight: 400
  filename: "Manjari-Regular.ttf"
  post_script_name: "Manjari-Regular"
  full_name: "Manjari Regular"
  copyright: "Copyright 2018 The Manjari Project Authors (https://gitlab.com/smc/fonts/manjari)"
}
fonts {
  name: "Manjari"
  style: "normal"
  weight: 700
  filename: "Manjari-Bold.ttf"
  post_script_name: "Manjari-Bold"
  full_name: "Manjari Bold"
  copyright: "Copyright 2018 The Manjari Project Authors (https://gitlab.com/smc/fonts/manjari)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "malayalam"
subsets: "menu"
source {
  repository_url: "https://gitlab.com/smc/fonts/manjari"
  commit: "8948773e572ce0b58d93b0f120f561a0b02e9853"
  files {
    source_file: "build/Manjari-Regular.ttf"
    dest_file: "Manjari-Regular.ttf"
  }
  files {
    source_file: "build/Manjari-Bold.ttf"
    dest_file: "Manjari-Bold.ttf"
  }
  files {
    source_file: "build/Manjari-Thin.ttf"
    dest_file: "Manjari-Thin.ttf"
  }
  branch: "master"
}
primary_script: "Mlym"
stroke: "SANS_SERIF"
classifications: "DISPLAY"
