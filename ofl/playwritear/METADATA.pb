name: "Playwrite AR"
designer: "TypeTogether, Veronika Burian, José Scaglione"
license: "OFL"
category: "HANDWRITING"
date_added: "2024-05-16"
fonts {
  name: "Playwrite AR"
  style: "normal"
  weight: 400
  filename: "PlaywriteAR[wght].ttf"
  post_script_name: "PlaywriteAR-Regular"
  full_name: "Playwrite AR Regular"
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
  commit: "c92b72cb8ae2e7458b5de4e0f8f08b0861c35afc"
  archive_url: "https://github.com/TypeTogether/Playwrite/releases/download/v1.003/Playwrite-fonts.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/PlaywriteAR[wght].ttf"
    dest_file: "PlaywriteAR[wght].ttf"
  }
  branch: "main"
}
display_name: "Playwrite Argentina"
minisite_url: "https://primarium.info/countries/argentina"
primary_language: "es_Latn"
