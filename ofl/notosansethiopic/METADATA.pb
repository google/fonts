name: "Noto Sans Ethiopic"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Ethiopic"
  style: "normal"
  weight: 400
  filename: "NotoSansEthiopic[wdth,wght].ttf"
  post_script_name: "NotoSansEthiopic-Regular"
  full_name: "Noto Sans Ethiopic Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/ethiopic)"
}
subsets: "ethiopic"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wdth"
  min_value: 62.5
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/ethiopic"
  archive_url: "https://github.com/notofonts/ethiopic/releases/download/NotoSansEthiopic-v2.102/NotoSansEthiopic-v2.102.zip"
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansEthiopic/googlefonts/variable-ttf/NotoSansEthiopic[wdth,wght].ttf"
    dest_file: "NotoSansEthiopic[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "am_Ethi"  # Amharic
languages: "byn_Ethi"  # Blin
languages: "gez_Ethi"  # Geez
languages: "om_Ethi"  # Oromo, Ethiopic
languages: "ti_Ethi"  # Tigrinya
languages: "tig_Ethi"  # Tigre
languages: "wal_Ethi"  # Wolaytta
primary_script: "Ethi"
