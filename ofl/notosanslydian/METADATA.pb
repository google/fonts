name: "Noto Sans Lydian"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Lydian"
  style: "normal"
  weight: 400
  filename: "NotoSansLydian-Regular.ttf"
  post_script_name: "NotoSansLydian-Regular"
  full_name: "Noto Sans Lydian Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/lydian)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "lydian"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/lydian"
  archive_url: "https://github.com/notofonts/lydian/releases/download/NotoSansLydian-v2.002/NotoSansLydian-v2.002.zip"
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
    source_file: "NotoSansLydian/googlefonts/ttf/NotoSansLydian-Regular.ttf"
    dest_file: "NotoSansLydian-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "xld_Lydi"  # Lydian
primary_script: "Lydi"
