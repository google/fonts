name: "Playwrite PE"
designer: "TypeTogether, Veronika Burian, José Scaglione"
license: "OFL"
category: "HANDWRITING"
date_added: "2024-05-16"
fonts {
  name: "Playwrite PE"
  style: "normal"
  weight: 400
  filename: "PlaywritePE[wght].ttf"
  post_script_name: "PlaywritePE-Regular"
  full_name: "Playwrite PE Regular"
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
    source_file: "fonts/variable/PlaywritePE[wght].ttf"
    dest_file: "PlaywritePE[wght].ttf"
  }
  branch: "main"
}
display_name: "Playwrite Perú"
minisite_url: "https://primarium.info/countries/peru"
primary_language: "es_Latn"