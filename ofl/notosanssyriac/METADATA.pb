name: "Noto Sans Syriac"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Syriac"
  style: "normal"
  weight: 400
  filename: "NotoSansSyriac[wght].ttf"
  post_script_name: "NotoSansSyriac-Regular"
  full_name: "Noto Sans Syriac Regular"
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
  archive_url: "https://github.com/notofonts/syriac/releases/download/NotoSansSyriac-v3.000/NotoSansSyriac-v3.000.zip"
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
    source_file: "NotoSansSyriac/googlefonts/variable-ttf/NotoSansSyriac[wght].ttf"
    dest_file: "NotoSansSyriac[wght].ttf"
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
