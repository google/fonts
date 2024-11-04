name: "Noto Sans Adlam"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Adlam"
  style: "normal"
  weight: 400
  filename: "NotoSansAdlam[wght].ttf"
  post_script_name: "NotoSansAdlam-Regular"
  full_name: "Noto Sans Adlam Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/adlam)"
}
subsets: "adlam"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/notofonts/adlam"
  archive_url: "https://github.com/notofonts/adlam/releases/download/NotoSansAdlam-v3.001/NotoSansAdlam-v3.001.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansAdlam/googlefonts/variable-ttf/NotoSansAdlam[wght].ttf"
    dest_file: "NotoSansAdlam[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "ff_Adlm"  # Fulah (Adlam)
languages: "fuf_Adlm"  # Pular, Adlam
primary_script: "Adlm"
