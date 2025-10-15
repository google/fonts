name: "Noto Sans Sinhala"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Sinhala"
  style: "normal"
  weight: 400
  filename: "NotoSansSinhala[wdth,wght].ttf"
  post_script_name: "NotoSansSinhala-Regular"
  full_name: "Noto Sans Sinhala Regular"
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
  commit: "032355e96de5bac83fd996535af3d13b1fbfeccf"
  archive_url: "https://github.com/notofonts/sinhala/releases/download/NotoSansSinhala-v3.000/NotoSansSinhala-v3.000.zip"
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
    source_file: "NotoSansSinhala/googlefonts/variable-ttf/NotoSansSinhala[wdth,wght].ttf"
    dest_file: "NotoSansSinhala[wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-sinhala.yaml"
}
is_noto: true
languages: "pi_Sinh"  # Pali (Sinhala)
languages: "sa_Sinh"  # Sanskrit (Sinhala)
languages: "si_Sinh"  # Sinhala
primary_script: "Sinh"
