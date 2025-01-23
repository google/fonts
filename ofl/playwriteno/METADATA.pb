name: "Playwrite NO"
designer: "TypeTogether, Veronika Burian, José Scaglione"
license: "OFL"
category: "HANDWRITING"
date_added: "2024-05-16"
fonts {
  name: "Playwrite NO"
  style: "normal"
  weight: 400
  filename: "PlaywriteNO[wght].ttf"
  post_script_name: "PlaywriteNO-Regular"
  full_name: "Playwrite NO Regular"
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
    source_file: "fonts/variable/PlaywriteNO[wght].ttf"
    dest_file: "PlaywriteNO[wght].ttf"
  }
  branch: "main"
}
display_name: "Playwrite Norge"
minisite_url: "https://primarium.info/countries/norway"
primary_language: "nb_Latn"