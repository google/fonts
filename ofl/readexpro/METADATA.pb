name: "Readex Pro"
designer: "Thomas Jockin, Nadine Chahine, Bonnie Shaver-Troup, Santiago Orozco, Héctor Gómez"
license: "OFL"
category: "SANS_SERIF"
date_added: "2021-09-16"
fonts {
  name: "Readex Pro"
  style: "normal"
  weight: 400
  filename: "ReadexPro[HEXP,wght].ttf"
  post_script_name: "ReadexPro-Regular"
  full_name: "Readex Pro Regular"
  copyright: "Copyright 2019 The Readex Pro Project Authors (https://github.com/ThomasJockin/readexpro)"
}
subsets: "arabic"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "HEXP"
  min_value: 0.0
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 160.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/ThomasJockin/readexpro"
  commit: "563dfbb36ae45e52ec50829b016ce724ac2fca70"
  files {
    source_file: "fonts/variable/Readexpro[HEXP,wght].ttf"
    dest_file: "ReadexPro[HEXP,wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
primary_script: "Arab"
