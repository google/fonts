name: "Noto Sans Linear B"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Linear B"
  style: "normal"
  weight: 400
  filename: "NotoSansLinearB-Regular.ttf"
  post_script_name: "NotoSansLinearB-Regular"
  full_name: "Noto Sans Linear B Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/linear-b)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "linear-b"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/linear-b"
  archive_url: "https://github.com/notofonts/linear-b/releases/download/NotoSansLinearB-v2.002/NotoSansLinearB-v2.002.zip"
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
    source_file: "NotoSansLinearB/googlefonts/ttf/NotoSansLinearB-Regular.ttf"
    dest_file: "NotoSansLinearB-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "gmy_Linb"  # Mycenaean Greek
languages: "grc_Linb"  # Ancient Greek, Linear B
primary_script: "Linb"
