name: "Brawler"
designer: "Cyreal"
license: "OFL"
category: "SERIF"
date_added: "2011-05-18"
fonts {
  name: "Brawler"
  style: "normal"
  weight: 400
  filename: "Brawler-Regular.ttf"
  post_script_name: "Brawler-Regular"
  full_name: "Brawler Regular"
  copyright: "Copyright 2011 The Brawler Project Authors (https://github.com/cyrealtype/Brawler)"
}
fonts {
  name: "Brawler"
  style: "normal"
  weight: 700
  filename: "Brawler-Bold.ttf"
  post_script_name: "Brawler-Bold"
  full_name: "Brawler Bold"
  copyright: "Copyright 2011 The Brawler Project Authors (https://github.com/cyrealtype/Brawler)"
}
subsets: "latin"
subsets: "menu"
source {
  repository_url: "https://github.com/cyrealtype/Brawler"
  commit: "a8e1fc6a4c43dedc38394c4f4086f526b72e852d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/TTF/Brawler-Regular.ttf"
    dest_file: "Brawler-Regular.ttf"
  }
  files {
    source_file: "fonts/TTF/Brawler-Bold.ttf"
    dest_file: "Brawler-Bold.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
