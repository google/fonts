name: "Noto Sans Anatolian Hieroglyphs"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Anatolian Hieroglyphs"
  style: "normal"
  weight: 400
  filename: "NotoSansAnatolianHieroglyphs-Regular.ttf"
  post_script_name: "NotoSansAnatolianHieroglyphs-Regular"
  full_name: "Noto Sans Anatolian Hieroglyphs Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/anatolian-hieroglyphs)"
}
subsets: "anatolian-hieroglyphs"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/anatolian-hieroglyphs"
  commit: "d82f0bce270456bb1e975e11b250f61cd1f0e8c7"
  archive_url: "https://github.com/notofonts/anatolian-hieroglyphs/releases/download/NotoSansAnatolianHieroglyphs-v2.001/NotoSansAnatolianHieroglyphs-v2.001.zip"
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
    source_file: "NotoSansAnatolianHieroglyphs/googlefonts/ttf/NotoSansAnatolianHieroglyphs-Regular.ttf"
    dest_file: "NotoSansAnatolianHieroglyphs-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-anatolian-hieroglyphs.yaml"
}
is_noto: true
languages: "hlu_Hluw"
primary_script: "Hluw"
