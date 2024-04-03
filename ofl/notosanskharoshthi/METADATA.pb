name: "Noto Sans Kharoshthi"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Kharoshthi"
  style: "normal"
  weight: 400
  filename: "NotoSansKharoshthi-Regular.ttf"
  post_script_name: "NotoSansKharoshthi-Regular"
  full_name: "Noto Sans Kharoshthi Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/kharoshthi)"
}
subsets: "kharoshthi"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/kharoshthi"
  archive_url: "https://github.com/notofonts/kharoshthi/releases/download/NotoSansKharoshthi-v2.004/NotoSansKharoshthi-v2.004.zip"
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
    source_file: "NotoSansKharoshthi/googlefonts/ttf/NotoSansKharoshthi-Regular.ttf"
    dest_file: "NotoSansKharoshthi-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "pra_Khar"  # Prakrit
languages: "sa_Khar"  # Sanskrit, Kharoshthi
primary_script: "Khar"
