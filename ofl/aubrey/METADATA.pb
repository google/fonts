name: "Aubrey"
designer: "Cyreal"
license: "OFL"
category: "DISPLAY"
date_added: "2011-07-27"
fonts {
  name: "Aubrey"
  style: "normal"
  weight: 400
  filename: "Aubrey-Regular.ttf"
  post_script_name: "Aubrey-Regular"
  full_name: "Aubrey Regular"
  copyright: "Copyright 2011 The Aubrey Project Authors (https://github.com/cyrealtype/Aubrey)"
}
subsets: "latin"
subsets: "menu"
source {
  repository_url: "https://github.com/cyrealtype/Aubrey"
  commit: "1946b0d99c0fec87702a59afc8b5b941a32e0171"
  config_yaml: "sources/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_US.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/TTF/Aubrey-Regular.ttf"
    dest_file: "Aubrey-Regular.ttf"
  }
  branch: "master"
}
