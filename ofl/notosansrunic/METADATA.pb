name: "Noto Sans Runic"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Runic"
  style: "normal"
  weight: 400
  filename: "NotoSansRunic-Regular.ttf"
  post_script_name: "NotoSansRunic-Regular"
  full_name: "Noto Sans Runic Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/runic)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "runic"
source {
  repository_url: "https://github.com/notofonts/runic"
  archive_url: "https://github.com/notofonts/runic/releases/download/NotoSansRunic-v2.002/NotoSansRunic-v2.002.zip"
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
    source_file: "NotoSansRunic/googlefonts/ttf/NotoSansRunic-Regular.ttf"
    dest_file: "NotoSansRunic-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "de_Runr"  # German, Runic
languages: "got_Runr"  # Gothic, Runic
languages: "non_Runr"  # Old Norse
primary_script: "Runr"
