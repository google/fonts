name: "Noto Sans Tamil"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Tamil"
  style: "normal"
  weight: 400
  filename: "NotoSansTamil[wdth,wght].ttf"
  post_script_name: "NotoSansTamil-Regular"
  full_name: "Noto Sans Tamil Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/tamil)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "tamil"
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
  repository_url: "https://github.com/notofonts/tamil"
  archive_url: "https://github.com/notofonts/tamil/releases/download/NotoSansTamil-v2.004/NotoSansTamil-v2.004.zip"
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
    source_file: "NotoSansTamil/googlefonts/variable-ttf/NotoSansTamil[wdth,wght].ttf"
    dest_file: "NotoSansTamil[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "bfq_Taml"  # Badaga
languages: "ta_Taml"  # Tamil
primary_script: "Taml"
