name: "Noto Sans Old Hungarian"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Old Hungarian"
  style: "normal"
  weight: 400
  filename: "NotoSansOldHungarian-Regular.ttf"
  post_script_name: "NotoSansOldHungarian-Regular"
  full_name: "Noto Sans Old Hungarian Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/old-hungarian)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "old-hungarian"
source {
  repository_url: "https://github.com/notofonts/old-hungarian"
  archive_url: "https://github.com/notofonts/old-hungarian/releases/download/NotoSansOldHungarian-v2.005/NotoSansOldHungarian-v2.005.zip"
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
    source_file: "NotoSansOldHungarian/googlefonts/ttf/NotoSansOldHungarian-Regular.ttf"
    dest_file: "NotoSansOldHungarian-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "ohu_Hung"  # Old Hungarian
