name: "Noto Sans Kaithi"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Kaithi"
  style: "normal"
  weight: 400
  filename: "NotoSansKaithi-Regular.ttf"
  post_script_name: "NotoSansKaithi-Regular"
  full_name: "Noto Sans Kaithi Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/kaithi)"
}
subsets: "kaithi"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/kaithi"
  archive_url: "https://github.com/notofonts/kaithi/releases/download/NotoSansKaithi-v2.005/NotoSansKaithi-v2.005.zip"
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
    source_file: "NotoSansKaithi/googlefonts/ttf/NotoSansKaithi-Regular.ttf"
    dest_file: "NotoSansKaithi-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "bho_Kthi"  # Bhojpuri, Kaithi
primary_script: "Kthi"
