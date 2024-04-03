name: "Noto Sans Elbasan"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Elbasan"
  style: "normal"
  weight: 400
  filename: "NotoSansElbasan-Regular.ttf"
  post_script_name: "NotoSansElbasan-Regular"
  full_name: "Noto Sans Elbasan Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/elbasan)"
}
subsets: "elbasan"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/elbasan"
  archive_url: "https://github.com/notofonts/elbasan/releases/download/NotoSansElbasan-v2.004/NotoSansElbasan-v2.004.zip"
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
    source_file: "NotoSansElbasan/googlefonts/ttf/NotoSansElbasan-Regular.ttf"
    dest_file: "NotoSansElbasan-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "sq_Elba"  # Albanian, Elbasan
primary_script: "Elba"
