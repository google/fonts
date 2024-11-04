name: "Noto Sans Javanese"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Javanese"
  style: "normal"
  weight: 400
  filename: "NotoSansJavanese[wght].ttf"
  post_script_name: "NotoSansJavanese-Regular"
  full_name: "Noto Sans Javanese Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/javanese)"
}
subsets: "javanese"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/notofonts/javanese"
  archive_url: "https://github.com/notofonts/javanese/releases/download/NotoSansJavanese-v2.005/NotoSansJavanese-v2.005.zip"
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansJavanese/googlefonts/variable-ttf/NotoSansJavanese[wght].ttf"
    dest_file: "NotoSansJavanese[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "jv_Java"  # Javanese, Javanese
primary_script: "Java"
