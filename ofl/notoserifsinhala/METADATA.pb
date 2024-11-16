name: "Noto Serif Sinhala"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Sinhala"
  style: "normal"
  weight: 400
  filename: "NotoSerifSinhala[wdth,wght].ttf"
  post_script_name: "NotoSerifSinhala-Regular"
  full_name: "Noto Serif Sinhala Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/sinhala)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "sinhala"
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
  repository_url: "https://github.com/notofonts/sinhala"
  archive_url: "https://github.com/notofonts/sinhala/releases/download/NotoSerifSinhala-v2.007/NotoSerifSinhala-v2.007.zip"
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
    source_file: "NotoSerifSinhala/googlefonts/variable-ttf/NotoSerifSinhala[wdth,wght].ttf"
    dest_file: "NotoSerifSinhala[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "pi_Sinh"  # Pali, Sinhala
languages: "sa_Sinh"  # Sanskrit, Sinhala
languages: "si_Sinh"  # Sinhala
primary_script: "Sinh"
