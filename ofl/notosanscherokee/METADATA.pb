name: "Noto Sans Cherokee"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Cherokee"
  style: "normal"
  weight: 400
  filename: "NotoSansCherokee[wght].ttf"
  post_script_name: "NotoSansCherokee-Regular"
  full_name: "Noto Sans Cherokee Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/cherokee)"
}
subsets: "cherokee"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/cherokee"
  archive_url: "https://github.com/notofonts/cherokee/releases/download/NotoSansCherokee-v2.001/NotoSansCherokee-v2.001.zip"
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
    source_file: "NotoSansCherokee/googlefonts/variable-ttf/NotoSansCherokee[wght].ttf"
    dest_file: "NotoSansCherokee[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "chr_Cher"  # Cherokee
primary_script: "Cher"
