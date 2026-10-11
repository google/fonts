name: "Creepster Caps"
designer: "Sideshow"
license: "APACHE2"
category: "DISPLAY"
date_added: "2011-10-24"
fonts {
  name: "Creepster Caps"
  style: "normal"
  weight: 400
  filename: "CreepsterCaps-Regular.ttf"
  post_script_name: "CreepsterCaps-Regular"
  full_name: "Creepster Caps Regular"
  copyright: "Copyright (c) 2010 by Font Diner, Inc DBA Sideshow (diner@fontdiner.com). All rights reserved."
}
subsets: "menu"
subsets: "latin"
source {
  repository_url: "https://github.com/googlefonts/creepstercaps"
  commit: "d2ba0c45feb25a88cfbdd1b28ae5fe0714d622a7"
  files {
    source_file: "LICENSE.txt"
    dest_file: "LICENSE.txt"
  }
  files {
    source_file: "fonts/ttf/CreepsterCaps-Regular.ttf"
    dest_file: "CreepsterCaps-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
