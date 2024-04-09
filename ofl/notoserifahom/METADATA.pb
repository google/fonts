name: "Noto Serif Ahom"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Ahom"
  style: "normal"
  weight: 400
  filename: "NotoSerifAhom-Regular.ttf"
  post_script_name: "NotoSerifAhom-Regular"
  full_name: "Noto Serif Ahom Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/ahom)"
}
subsets: "ahom"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/ahom"
  archive_url: "https://github.com/notofonts/ahom/releases/download/NotoSerifAhom-v2.007/NotoSerifAhom-v2.007.zip"
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
    source_file: "NotoSerifAhom/googlefonts/ttf/NotoSerifAhom-Regular.ttf"
    dest_file: "NotoSerifAhom-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "aho_Ahom"  # Ahom
languages: "sa_Ahom"  # Sanskrit, Ahom
primary_script: "Ahom"
