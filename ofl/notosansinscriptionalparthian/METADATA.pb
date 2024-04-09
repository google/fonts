name: "Noto Sans Inscriptional Parthian"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Inscriptional Parthian"
  style: "normal"
  weight: 400
  filename: "NotoSansInscriptionalParthian-Regular.ttf"
  post_script_name: "NotoSansInscriptionalParthian-Regular"
  full_name: "Noto Sans Inscriptional Parthian Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/inscriptional-parthian)"
}
subsets: "inscriptional-parthian"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/inscriptional-parthian"
  archive_url: "https://github.com/notofonts/inscriptional-parthian/releases/download/NotoSansInscriptionalParthian-v2.003/NotoSansInscriptionalParthian-v2.003.zip"
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
    source_file: "NotoSansInscriptionalParthian/googlefonts/ttf/NotoSansInscriptionalParthian-Regular.ttf"
    dest_file: "NotoSansInscriptionalParthian-Regular.ttf"
  }
  branch: "main"
}
is_noto: true
languages: "aii_Prti"  # Assyrian Neo-Aramaic, Inscriptional Parthian
languages: "xpr_Prti"  # Parthian
primary_script: "Prti"
