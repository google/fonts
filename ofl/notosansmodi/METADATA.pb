name: "Noto Sans Modi"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Modi"
  style: "normal"
  weight: 400
  filename: "NotoSansModi-Regular.ttf"
  post_script_name: "NotoSansModi-Regular"
  full_name: "Noto Sans Modi Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/modi)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "modi"
source {
  repository_url: "https://github.com/notofonts/modi"
  archive_url: "https://github.com/notofonts/modi/releases/download/NotoSansModi-v2.004/NotoSansModi-v2.004.zip"
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
    source_file: "NotoSansModi/googlefonts/ttf/NotoSansModi-Regular.ttf"
    dest_file: "NotoSansModi-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "mr_Modi"  # Marathi, Modi
languages: "sa_Modi"  # Sanskrit, Modi
primary_script: "Modi"
