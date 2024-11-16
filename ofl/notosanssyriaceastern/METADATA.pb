name: "Noto Sans Syriac Eastern"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-01-06"
fonts {
  name: "Noto Sans Syriac Eastern"
  style: "normal"
  weight: 400
  filename: "NotoSansSyriacEastern[wght].ttf"
  post_script_name: "NotoSansSyriacEastern-Regular"
  full_name: "Noto Sans Syriac Eastern Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/syriac)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "syriac"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/syriac"
  archive_url: "https://github.com/notofonts/syriac/releases/download/NotoSansSyriacEastern-v3.001/NotoSansSyriacEastern-v3.001.zip"
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
    source_file: "NotoSansSyriacEastern/googlefonts/variable-ttf/NotoSansSyriacEastern[wght].ttf"
    dest_file: "NotoSansSyriacEastern[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "aii_Syrc"  # Assyrian Neo-Aramaic
languages: "ar_Syrc"  # Arabic, Syriac
languages: "syc_Syrc"  # Classical Syriac
languages: "syr_Syrc"  # Syriac
languages: "tru_Syrc"  # Turoyo, Syriac
primary_script: "Syrc"
