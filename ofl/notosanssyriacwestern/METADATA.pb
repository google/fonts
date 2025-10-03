name: "Noto Sans Syriac Western"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-01-06"
fonts {
  name: "Noto Sans Syriac Western"
  style: "normal"
  weight: 400
  filename: "NotoSansSyriacWestern[wght].ttf"
  post_script_name: "NotoSansSyriacWestern-Regular"
  full_name: "Noto Sans Syriac Western Regular"
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
  commit: "a24ba4586441a6b76df20215464898852e702078"
  archive_url: "https://github.com/notofonts/syriac/releases/download/NotoSansSyriacWestern-v3.001/NotoSansSyriacWestern-v3.001.zip"
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
    source_file: "NotoSansSyriacWestern/googlefonts/variable-ttf/NotoSansSyriacWestern[wght].ttf"
    dest_file: "NotoSansSyriacWestern[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "aii_Syrc"  # Assyrian Neo-Aramaic
languages: "ar_Syrc"  # Arabic (Syriac)
languages: "syc_Syrc"  # Classical Syriac
languages: "syr_Syrc"  # Syriac
languages: "tru_Syrc"  # Turoyo (Syriac)
primary_script: "Syrc"
