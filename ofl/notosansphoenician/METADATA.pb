name: "Noto Sans Phoenician"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Phoenician"
  style: "normal"
  weight: 400
  filename: "NotoSansPhoenician-Regular.ttf"
  post_script_name: "NotoSansPhoenician-Regular"
  full_name: "Noto Sans Phoenician Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/phoenician)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "phoenician"
source {
  repository_url: "https://github.com/notofonts/phoenician"
  archive_url: "https://github.com/notofonts/phoenician/releases/download/NotoSansPhoenician-v2.001/NotoSansPhoenician-v2.001.zip"
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
    source_file: "NotoSansPhoenician/googlefonts/ttf/NotoSansPhoenician-Regular.ttf"
    dest_file: "NotoSansPhoenician-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "aii_Phnx"  # Assyrian Neo-Aramaic, Phoenician
languages: "phn_Phnx"  # Phoenician
primary_script: "Phnx"
