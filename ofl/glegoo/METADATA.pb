name: "Glegoo"
designer: "Eduardo Tunni"
license: "OFL"
category: "SERIF"
date_added: "2012-01-25"
fonts {
  name: "Glegoo"
  style: "normal"
  weight: 400
  filename: "Glegoo-Regular.ttf"
  post_script_name: "Glegoo-Regular"
  full_name: "Glegoo"
  copyright: "Copyright (c) 2011, Eduardo Tunni (http://www.tipo.net.ar), Copyright 2011-13 Lohit Fonts Project contributors (http://fedorahosted.org/lohit)"
}
fonts {
  name: "Glegoo"
  style: "normal"
  weight: 700
  filename: "Glegoo-Bold.ttf"
  post_script_name: "Glegoo-Bold"
  full_name: "Glegoo Bold"
  copyright: "Copyright (c) 2011, Eduardo Tunni (http://www.tipo.net.ar), Copyright 2011-13 Lohit Fonts Project contributors (http://fedorahosted.org/lohit)"
}
subsets: "menu"
subsets: "devanagari"
subsets: "latin"
subsets: "latin-ext"
source {
  repository_url: "https://github.com/googlefonts/glegoo"
  commit: "f33250e4771fc7535fbbe847c4d9787396dff0a9"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Glegoo-Bold.ttf"
    dest_file: "Glegoo-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Glegoo-Regular.ttf"
    dest_file: "Glegoo-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
stroke: "SLAB_SERIF"
