name: "Noto Serif Hebrew"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Hebrew"
  style: "normal"
  weight: 400
  filename: "NotoSerifHebrew[wdth,wght].ttf"
  post_script_name: "NotoSerifHebrew-Regular"
  full_name: "Noto Serif Hebrew Regular"
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
  archive_url: "https://github.com/notofonts/hebrew/releases/download/NotoSerifHebrew-v2.003/NotoSerifHebrew-v2.003.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSerifHebrew/googlefonts/variable-ttf/NotoSerifHebrew[wdth,wght].ttf"
    dest_file: "NotoSerifHebrew[wdth,wght].ttf"
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
