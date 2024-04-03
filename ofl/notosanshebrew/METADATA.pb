name: "Noto Sans Hebrew"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Hebrew"
  style: "normal"
  weight: 400
  filename: "NotoSansHebrew[wdth,wght].ttf"
  post_script_name: "NotoSansHebrew-Regular"
  full_name: "Noto Sans Hebrew Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/hebrew)"
}
subsets: "hebrew"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
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
  repository_url: "https://github.com/notofonts/hebrew"
  archive_url: "https://github.com/notofonts/hebrew/releases/download/NotoSansHebrew-v2.003/NotoSansHebrew-v2.003.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansHebrew/googlefonts/variable-ttf/NotoSansHebrew[wdth,wght].ttf"
    dest_file: "NotoSansHebrew[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "he_Hebr"  # Hebrew
languages: "jpr_Hebr"  # Judeo-Persian
languages: "jrb_Hebr"  # Judeo-Arabic
languages: "lad_Hebr"  # Ladino
languages: "sam_Hebr"  # Samaritan Aramaic
languages: "yi_Hebr"  # Yiddish
languages: "zh_Hebr"  # Chinese, Hebrew
primary_script: "Hebr"
