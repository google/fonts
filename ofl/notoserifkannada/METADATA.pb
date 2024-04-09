name: "Noto Serif Kannada"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Kannada"
  style: "normal"
  weight: 400
  filename: "NotoSerifKannada[wght].ttf"
  post_script_name: "NotoSerifKannada-Regular"
  full_name: "Noto Serif Kannada Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/kannada)"
}
subsets: "kannada"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/kannada"
  archive_url: "https://github.com/notofonts/kannada/releases/download/NotoSerifKannada-v2.005/NotoSerifKannada-v2.005.zip"
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
    source_file: "NotoSerifKannada/googlefonts/variable/NotoSerifKannada[wght].ttf"
    dest_file: "NotoSerifKannada[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "kn_Knda"  # Kannada
languages: "tcy_Knda"  # Tulu
primary_script: "Knda"
