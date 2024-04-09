name: "Noto Sans Malayalam"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Malayalam"
  style: "normal"
  weight: 400
  filename: "NotoSansMalayalam[wdth,wght].ttf"
  post_script_name: "NotoSansMalayalam-Regular"
  full_name: "Noto Sans Malayalam Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/malayalam)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "malayalam"
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
  repository_url: "https://github.com/notofonts/malayalam"
  archive_url: "https://github.com/notofonts/malayalam/releases/download/NotoSansMalayalam-v2.104/NotoSansMalayalam-v2.104.zip"
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
    source_file: "NotoSansMalayalam/googlefonts/variable-ttf/NotoSansMalayalam[wdth,wght].ttf"
    dest_file: "NotoSansMalayalam[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "ml_Mlym"  # Malayalam
primary_script: "Mlym"
