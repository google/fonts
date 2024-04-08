name: "Noto Sans Khmer"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Khmer"
  style: "normal"
  weight: 400
  filename: "NotoSansKhmer[wdth,wght].ttf"
  post_script_name: "NotoSansKhmer-Regular"
  full_name: "Noto Sans Khmer Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/khmer)"
}
subsets: "khmer"
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
  repository_url: "https://github.com/notofonts/khmer"
  archive_url: "https://github.com/notofonts/khmer/releases/download/NotoSansKhmer-v2.004/NotoSansKhmer-v2.004.zip"
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
    source_file: "NotoSansKhmer/googlefonts/variable/NotoSansKhmer[wdth,wght].ttf"
    dest_file: "NotoSansKhmer[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "km_Khmr"  # Khmer
primary_script: "Khmr"
