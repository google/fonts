name: "Noto Sans Takri"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Takri"
  style: "normal"
  weight: 400
  filename: "NotoSansTakri-Regular.ttf"
  post_script_name: "NotoSansTakri-Regular"
  full_name: "Noto Sans Takri Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/takri)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "takri"
source {
  repository_url: "https://github.com/notofonts/takri"
  archive_url: "https://github.com/notofonts/takri/releases/download/NotoSansTakri-v2.005/NotoSansTakri-v2.005.zip"
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
    source_file: "NotoSansTakri/googlefonts/ttf/NotoSansTakri-Regular.ttf"
    dest_file: "NotoSansTakri-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "doi_Takr"  # Dogri, Takri
primary_script: "Takr"
