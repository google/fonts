name: "Noto Sans Thaana"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Thaana"
  style: "normal"
  weight: 400
  filename: "NotoSansThaana[wght].ttf"
  post_script_name: "NotoSansThaana-Regular"
  full_name: "Noto Sans Thaana Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/thaana)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "thaana"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/thaana"
  archive_url: "https://github.com/notofonts/thaana/releases/download/NotoSansThaana-v3.001/NotoSansThaana-v3.001.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "NotoSansThaana/googlefonts/variable/NotoSansThaana[wght].ttf"
    dest_file: "NotoSansThaana[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "dv_Thaa"  # Divehi
primary_script: "Thaa"
