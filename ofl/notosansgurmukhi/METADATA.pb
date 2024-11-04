name: "Noto Sans Gurmukhi"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Gurmukhi"
  style: "normal"
  weight: 400
  filename: "NotoSansGurmukhi[wdth,wght].ttf"
  post_script_name: "NotoSansGurmukhi-Regular"
  full_name: "Noto Sans Gurmukhi Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/gurmukhi)"
}
subsets: "gurmukhi"
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
  repository_url: "https://github.com/notofonts/gurmukhi"
  archive_url: "https://github.com/notofonts/gurmukhi/releases/download/NotoSansGurmukhi-v2.004/NotoSansGurmukhi-v2.004.zip"
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
    source_file: "NotoSansGurmukhi/googlefonts/variable-ttf/NotoSansGurmukhi[wdth,wght].ttf"
    dest_file: "NotoSansGurmukhi[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "pa_Guru"  # Punjabi
primary_script: "Guru"
