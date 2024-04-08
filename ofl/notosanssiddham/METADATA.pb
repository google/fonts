name: "Noto Sans Siddham"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Siddham"
  style: "normal"
  weight: 400
  filename: "NotoSansSiddham-Regular.ttf"
  post_script_name: "NotoSansSiddham-Regular"
  full_name: "Noto Sans Siddham Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/siddham)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "siddham"
source {
  repository_url: "https://github.com/notofonts/siddham"
  archive_url: "https://github.com/notofonts/siddham/releases/download/NotoSansSiddham-v2.005/NotoSansSiddham-v2.005.zip"
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
    source_file: "NotoSansSiddham/googlefonts/ttf/NotoSansSiddham-Regular.ttf"
    dest_file: "NotoSansSiddham-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "sa_Sidd"  # Sanskrit, Siddham
primary_script: "Sidd"
