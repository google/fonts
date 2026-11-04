name: "Astloch"
designer: "Dan Rhatigan"
license: "OFL"
category: "DISPLAY"
date_added: "2011-02-16"
source {
  repository_url: "https://github.com/googlefonts/astloch"
  commit: "e6ac0a83f48c458c055180c7fb695732d6b5559a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Astloch-Bold.ttf"
    dest_file: "Astloch-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Astloch-Regular.ttf"
    dest_file: "Astloch-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}

fonts {
  name: "Astloch"
  style: "normal"
  weight: 400
  filename: "Astloch-Regular.ttf"
  post_script_name: "Astloch-Regular"
  full_name: "Astloch Regular"
  copyright: "Copyright 2011 The Astloch Project Authors"
}
fonts {
  name: "Astloch"
  style: "normal"
  weight: 700
  filename: "Astloch-Bold.ttf"
  post_script_name: "Astloch-Bold"
  full_name: "Astloch Bold"
  copyright: ""
}
subsets: "latin"
subsets: "menu"
