name: "Noto Sans Mandaic"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Mandaic"
  style: "normal"
  weight: 400
  filename: "NotoSansMandaic-Regular.ttf"
  post_script_name: "NotoSansMandaic-Regular"
  full_name: "Noto Sans Mandaic Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/mandaic)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "mandaic"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/mandaic"
  archive_url: "https://github.com/notofonts/mandaic/releases/download/NotoSansMandaic-v2.002/NotoSansMandaic-v2.002.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSansMandaic/googlefonts/ttf/NotoSansMandaic-Regular.ttf"
    dest_file: "NotoSansMandaic-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "myz_Mand"  # Mandaic
primary_script: "Mand"
