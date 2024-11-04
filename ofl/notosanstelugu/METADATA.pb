name: "Noto Sans Telugu"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Telugu"
  style: "normal"
  weight: 400
  filename: "NotoSansTelugu[wdth,wght].ttf"
  post_script_name: "NotoSansTelugu-Regular"
  full_name: "Noto Sans Telugu Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/telugu)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "telugu"
axes {
  tag: "wdth"
  min_value: 62.5
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/telugu"
  archive_url: "https://github.com/notofonts/telugu/releases/download/NotoSansTelugu-v2.005/NotoSansTelugu-v2.005.zip"
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansTelugu/googlefonts/variable/NotoSansTelugu[wdth,wght].ttf"
    dest_file: "NotoSansTelugu[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "gon_Telu"  # Gondi, Telugu
languages: "lmn_Telu"  # Lambadi
languages: "te_Telu"  # Telugu
languages: "wbq_Telu"  # Waddar
primary_script: "Telu"
