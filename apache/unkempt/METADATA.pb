name: "Unkempt"
designer: "Sideshow"
license: "APACHE2"
category: "DISPLAY"
date_added: "2011-12-05"
fonts {
  name: "Unkempt"
  style: "normal"
  weight: 400
  filename: "Unkempt-Regular.ttf"
  post_script_name: "Unkempt-Regular"
  full_name: "Unkempt Regular"
  copyright: "Copyright (c) 2010 by Font Diner, Inc DBA Sideshow. All rights reserved."
}
fonts {
  name: "Unkempt"
  style: "normal"
  weight: 700
  filename: "Unkempt-Bold.ttf"
  post_script_name: "Unkempt-Bold"
  full_name: "Unkempt Bold"
  copyright: "Copyright (c) 2011 by Font Diner, Inc DBA Sideshow (diner@fontdiner.com) with Reseved Font Name \"Unkempt Bold\""
}
subsets: "latin"
subsets: "menu"
classifications: "DISPLAY"
classifications: "HANDWRITING"
source {
  repository_url: "https://github.com/googlefonts/unkempt"
  commit: "ef6ca68e4a2a244ac75907c9a6b8e9d0ca7070cb"
  files {
    source_file: "LICENSE.txt"
    dest_file: "LICENSE.txt"
  }
  files {
    source_file: "fonts/ttf/Unkempt-Bold.ttf"
    dest_file: "Unkempt-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Unkempt-Regular.ttf"
    dest_file: "Unkempt-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
