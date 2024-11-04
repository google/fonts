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
  post_script_name: "NotoSansHebrew-Thin"
  full_name: "Noto Sans Hebrew Thin"
  copyright: "Copyright 2024 The Noto Project Authors (https://github.com/notofonts/hebrew)"
}
subsets: "cyrillic-ext"
subsets: "greek-ext"
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
  commit: "036f3206f67caac235cf8546a7751d3440771a7e"
  archive_url: "https://github.com/notofonts/hebrew/releases/download/NotoSansHebrew-v3.001/NotoSansHebrew-v3.001.zip"
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
