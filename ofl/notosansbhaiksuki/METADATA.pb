name: "Noto Sans Bhaiksuki"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Bhaiksuki"
  style: "normal"
  weight: 400
  filename: "NotoSansBhaiksuki-Regular.ttf"
  post_script_name: "NotoSansBhaiksuki-Regular"
  full_name: "Noto Sans Bhaiksuki Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/bhaiksuki)"
}
subsets: "bhaiksuki"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/bhaiksuki"
  archive_url: "https://github.com/notofonts/bhaiksuki/releases/download/NotoSansBhaiksuki-v2.002/NotoSansBhaiksuki-v2.002.zip"
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
    source_file: "NotoSansBhaiksuki/googlefonts/ttf/NotoSansBhaiksuki-Regular.ttf"
    dest_file: "NotoSansBhaiksuki-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "sa_Bhks"  # Sanskrit, Bhaiksuki
primary_script: "Bhks"
