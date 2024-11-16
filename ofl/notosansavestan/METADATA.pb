name: "Noto Sans Avestan"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Avestan"
  style: "normal"
  weight: 400
  filename: "NotoSansAvestan-Regular.ttf"
  post_script_name: "NotoSansAvestan-Regular"
  full_name: "Noto Sans Avestan Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/avestan)"
}
subsets: "avestan"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/avestan"
  archive_url: "https://github.com/notofonts/avestan/releases/download/NotoSansAvestan-v2.003/NotoSansAvestan-v2.003.zip"
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
    source_file: "NotoSansAvestan/googlefonts/ttf/NotoSansAvestan-Regular.ttf"
    dest_file: "NotoSansAvestan-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "ae_Avst"  # Avestan
primary_script: "Avst"
