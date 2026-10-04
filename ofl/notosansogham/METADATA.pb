name: "Noto Sans Ogham"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Ogham"
  style: "normal"
  weight: 400
  filename: "NotoSansOgham-Regular.ttf"
  post_script_name: "NotoSansOgham-Regular"
  full_name: "Noto Sans Ogham Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/ogham)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "ogham"
source {
  repository_url: "https://github.com/notofonts/ogham"
  commit: "f9ef276aefef0c9442f613db21f69a02d4102888"
  archive_url: "https://github.com/notofonts/ogham/releases/download/NotoSansOgham-v2.001/NotoSansOgham-v2.001.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "NotoSansOgham/googlefonts/ttf/NotoSansOgham-Regular.ttf"
    dest_file: "NotoSansOgham-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-ogham.yaml"
}
is_noto: true
languages: "sga_Ogam"
primary_script: "Ogam"
