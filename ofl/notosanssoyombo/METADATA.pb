name: "Noto Sans Soyombo"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Soyombo"
  style: "normal"
  weight: 400
  filename: "NotoSansSoyombo-Regular.ttf"
  post_script_name: "NotoSansSoyombo-Regular"
  full_name: "Noto Sans Soyombo Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/soyombo)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "soyombo"
source {
  repository_url: "https://github.com/notofonts/soyombo"
  archive_url: "https://github.com/notofonts/soyombo/releases/download/NotoSansSoyombo-v2.001/NotoSansSoyombo-v2.001.zip"
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansSoyombo/googlefonts/ttf/NotoSansSoyombo-Regular.ttf"
    dest_file: "NotoSansSoyombo-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "cmg_Soyo"  # Classical Mongolian
languages: "sa_Soyo"  # Sanskrit, Soyombo
primary_script: "Soyo"
