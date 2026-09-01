name: "Gudea"
designer: "Agustina Mingote"
license: "OFL"
category: "SANS_SERIF"
date_added: "2012-01-18"
fonts {
  name: "Gudea"
  style: "normal"
  weight: 400
  filename: "Gudea-Regular.ttf"
  post_script_name: "Gudea"
  full_name: "Gudea"
  copyright: "Copyright (c) 2012, Agustina Mingote (agustinamingote@gmail.com), with Reserved Font Names \"Gudea\""
}
fonts {
  name: "Gudea"
  style: "italic"
  weight: 400
  filename: "Gudea-Italic.ttf"
  post_script_name: "Gudea-Italic"
  full_name: "Gudea Italic"
  copyright: "Copyright (c) 2012, Agustina Mingote (agustinamingote@gmail.com), with Reserved Font Names \"Gudea\""
}
fonts {
  name: "Gudea"
  style: "normal"
  weight: 700
  filename: "Gudea-Bold.ttf"
  post_script_name: "Gudea-Bold"
  full_name: "Gudea Bold"
  copyright: "Copyright (c) 2012, Agustina Mingote (agustinamingote@gmail.com), with Reserved Font Names \"Gudea\""
}
subsets: "menu"
subsets: "latin"
subsets: "latin-ext"
source {
  repository_url: "https://github.com/googlefonts/gudea"
  commit: "7651bdceeaa8148f45ee5781d87914346be8e9bc"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Gudea-Bold.ttf"
    dest_file: "Gudea-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Gudea-Italic.ttf"
    dest_file: "Gudea-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/Gudea-Regular.ttf"
    dest_file: "Gudea-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
