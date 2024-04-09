name: "Noto Serif Malayalam"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Malayalam"
  style: "normal"
  weight: 400
  filename: "NotoSerifMalayalam[wght].ttf"
  post_script_name: "NotoSerifMalayalam-Regular"
  full_name: "Noto Serif Malayalam Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/malayalam)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "malayalam"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/malayalam"
  archive_url: "https://github.com/notofonts/malayalam/releases/download/NotoSerifMalayalam-v2.104/NotoSerifMalayalam-v2.104.zip"
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
    source_file: "NotoSerifMalayalam/googlefonts/variable-ttf/NotoSerifMalayalam[wght].ttf"
    dest_file: "NotoSerifMalayalam[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "ml_Mlym"  # Malayalam
primary_script: "Mlym"
