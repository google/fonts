name: "Noto Sans Georgian"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Georgian"
  style: "normal"
  weight: 400
  filename: "NotoSansGeorgian[wdth,wght].ttf"
  post_script_name: "NotoSansGeorgian-Regular"
  full_name: "Noto Sans Georgian Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/georgian)"
}
subsets: "cyrillic-ext"
subsets: "georgian"
subsets: "greek-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "symbols"
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
  repository_url: "https://github.com/notofonts/georgian"
  archive_url: "https://github.com/notofonts/georgian/releases/download/NotoSansGeorgian-v2.005/NotoSansGeorgian-v2.005.zip"
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
    source_file: "NotoSansGeorgian/googlefonts/variable/NotoSansGeorgian[wdth,wght].ttf"
    dest_file: "NotoSansGeorgian[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "ka_Geor"  # Georgian
languages: "lzz_Geor"  # Laz
languages: "xmf_Geor"  # Mingrelian
primary_script: "Geor"
