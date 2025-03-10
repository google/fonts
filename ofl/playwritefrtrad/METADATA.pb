name: "Playwrite FR Trad"
designer: "TypeTogether, Veronika Burian, José Scaglione"
license: "OFL"
category: "HANDWRITING"
date_added: "2023-12-12"
fonts {
  name: "Playwrite FR Trad"
  style: "normal"
  weight: 400
  filename: "PlaywriteFRTrad[wght].ttf"
  post_script_name: "PlaywriteFRTrad-Regular"
  full_name: "Playwrite FR Trad Regular"
  copyright: "Copyright 2023 The Playwrite Project Authors (https://github.com/TypeTogether/Playwrite)"
}
# We use only the menu subset to avoid the subsetter issues identified with the PW fonts.
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 400.0
}
source {
  repository_url: "https://github.com/TypeTogether/Playwrite"
  archive_url: "https://github.com/TypeTogether/Playwrite/releases/download/v1.003/Playwrite-fonts.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/PlaywriteFRTrad[wght].ttf"
    dest_file: "PlaywriteFRTrad[wght].ttf"
  }
  branch: "main"
}
display_name: "Playwrite France Traditionnelle"
minisite_url: "https://primarium.info/countries/france"
primary_language: "fr_Latn"