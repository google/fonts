name: "Noto Serif Gurmukhi"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Gurmukhi"
  style: "normal"
  weight: 400
  filename: "NotoSerifGurmukhi[wght].ttf"
  post_script_name: "NotoSerifGurmukhi-Regular"
  full_name: "Noto Serif Gurmukhi Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/gurmukhi)"
}
subsets: "gurmukhi"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/gurmukhi"
  archive_url: "https://github.com/notofonts/gurmukhi/releases/download/NotoSerifGurmukhi-v2.004/NotoSerifGurmukhi-v2.004.zip"
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
    source_file: "NotoSerifGurmukhi/googlefonts/variable-ttf/NotoSerifGurmukhi[wght].ttf"
    dest_file: "NotoSerifGurmukhi[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "pa_Guru"  # Punjabi
primary_script: "Guru"
