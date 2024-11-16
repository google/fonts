name: "Noto Sans Glagolitic"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Glagolitic"
  style: "normal"
  weight: 400
  filename: "NotoSansGlagolitic-Regular.ttf"
  post_script_name: "NotoSansGlagolitic-Regular"
  full_name: "Noto Sans Glagolitic Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/glagolitic)"
}
subsets: "cyrillic-ext"
subsets: "glagolitic"
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "symbols"
source {
  repository_url: "https://github.com/notofonts/glagolitic"
  archive_url: "https://github.com/notofonts/glagolitic/releases/download/NotoSansGlagolitic-v2.004/NotoSansGlagolitic-v2.004.zip"
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
    source_file: "NotoSansGlagolitic/googlefonts/ttf/NotoSansGlagolitic-Regular.ttf"
    dest_file: "NotoSansGlagolitic-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "cu_Glag"  # Church Slavic, Glagolitic
primary_script: "Glag"
