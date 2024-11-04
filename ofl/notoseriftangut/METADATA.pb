name: "Noto Serif Tangut"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Tangut"
  style: "normal"
  weight: 400
  filename: "NotoSerifTangut-Regular.ttf"
  post_script_name: "NotoSerifTangut-Regular"
  full_name: "Noto Serif Tangut Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/tangut)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "tangut"
source {
  repository_url: "https://github.com/notofonts/tangut"
  archive_url: "https://github.com/notofonts/tangut/releases/download/NotoSerifTangut-v2.169/NotoSerifTangut-v2.169.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSerifTangut/googlefonts/ttf/NotoSerifTangut-Regular.ttf"
    dest_file: "NotoSerifTangut-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "txg_Tang"  # Tangut
primary_script: "Tang"
