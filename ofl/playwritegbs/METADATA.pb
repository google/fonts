name: "Playwrite GB S"
designer: "TypeTogether, Veronika Burian, José Scaglione"
license: "OFL"
category: "HANDWRITING"
date_added: "2024-01-18"
fonts {
  name: "Playwrite GB S"
  style: "normal"
  weight: 400
  filename: "PlaywriteGBS[wght].ttf"
  post_script_name: "PlaywriteGBS-Regular"
  full_name: "Playwrite GB S Regular"
  copyright: "Copyright 2023 The Playwrite Project Authors (https://github.com/TypeTogether/Playwrite)"
}
fonts {
  name: "Playwrite GB S"
  style: "italic"
  weight: 400
  filename: "PlaywriteGBS-Italic[wght].ttf"
  post_script_name: "PlaywriteGBS-Italic"
  full_name: "Playwrite GB S Italic"
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
    source_file: "fonts/variable/PlaywriteGBS[wght].ttf"
    dest_file: "PlaywriteGBS[wght].ttf"
  }
  files {
    source_file: "fonts/variable/PlaywriteGBS-Italic[wght].ttf"
    dest_file: "PlaywriteGBS-Italic[wght].ttf"
  }
  branch: "main"
}
display_name: "Playwrite England SemiJoined"
minisite_url: "https://primarium.info/countries/england"
primary_language: "en_Latn"