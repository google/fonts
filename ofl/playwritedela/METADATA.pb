name: "Playwrite DE LA"
designer: "TypeTogether, Veronika Burian, José Scaglione"
license: "OFL"
category: "HANDWRITING"
date_added: "2024-05-16"
fonts {
  name: "Playwrite DE LA"
  style: "normal"
  weight: 400
  filename: "PlaywriteDELA[wght].ttf"
  post_script_name: "PlaywriteDELA-Regular"
  full_name: "Playwrite DE LA Regular"
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
    source_file: "fonts/variable/PlaywriteDELA[wght].ttf"
    dest_file: "PlaywriteDELA[wght].ttf"
  }
  branch: "main"
}
display_name: "Playwrite Deutschland Lateinische Ausgangsschrift"
minisite_url: "https://primarium.info/countries/germany"
primary_language: "de_Latn"