name: "Noto Sans Hanunoo"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Hanunoo"
  style: "normal"
  weight: 400
  filename: "NotoSansHanunoo-Regular.ttf"
  post_script_name: "NotoSansHanunoo-Regular"
  full_name: "Noto Sans Hanunoo Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/hanunoo)"
}
subsets: "hanunoo"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/hanunoo"
  archive_url: "https://github.com/notofonts/hanunoo/releases/download/NotoSansHanunoo-v2.004/NotoSansHanunoo-v2.004.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansHanunoo/googlefonts/ttf/NotoSansHanunoo-Regular.ttf"
    dest_file: "NotoSansHanunoo-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "hnn_Hano"  # Hanunoo, Hanunoo
primary_script: "Hano"
