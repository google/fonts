name: "Noto Sans Old Turkic"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Old Turkic"
  style: "normal"
  weight: 400
  filename: "NotoSansOldTurkic-Regular.ttf"
  post_script_name: "NotoSansOldTurkic-Regular"
  full_name: "Noto Sans Old Turkic Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/old-turkic)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "old-turkic"
source {
  repository_url: "https://github.com/notofonts/old-turkic"
  archive_url: "https://github.com/notofonts/old-turkic/releases/download/NotoSansOldTurkic-v2.003/NotoSansOldTurkic-v2.003.zip"
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
    source_file: "NotoSansOldTurkic/googlefonts/ttf/NotoSansOldTurkic-Regular.ttf"
    dest_file: "NotoSansOldTurkic-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "otk_Orkh"  # Old Turkish
primary_script: "Orkh"
