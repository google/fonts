name: "Noto Sans Lao"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Lao"
  style: "normal"
  weight: 400
  filename: "NotoSansLao[wdth,wght].ttf"
  post_script_name: "NotoSansLao-Regular"
  full_name: "Noto Sans Lao Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/lao)"
}
subsets: "lao"
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
  repository_url: "https://github.com/notofonts/lao"
  archive_url: "https://github.com/notofonts/lao/releases/download/NotoSansLao-v2.003/NotoSansLao-v2.003.zip"
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSansLao/googlefonts/variable-ttf/NotoSansLao[wdth,wght].ttf"
    dest_file: "NotoSansLao[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "hnj_Laoo"  # Mong Njua
languages: "kjg_Laoo"  # Khmu
languages: "lo_Laoo"  # Lao
primary_script: "Laoo"
