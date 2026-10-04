name: "Noto Sans Manichaean"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Manichaean"
  style: "normal"
  weight: 400
  filename: "NotoSansManichaean-Regular.ttf"
  post_script_name: "NotoSansManichaean-Regular"
  full_name: "Noto Sans Manichaean Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/manichaean)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "manichaean"
subsets: "menu"
source {
  repository_url: "https://github.com/notofonts/manichaean"
  commit: "d3d108ab2cdf0250927b267fab4d2c8dea07dd68"
  archive_url: "https://github.com/notofonts/manichaean/releases/download/NotoSansManichaean-v2.005/NotoSansManichaean-v2.005.zip"
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
    source_file: "NotoSansManichaean/googlefonts/ttf/NotoSansManichaean-Regular.ttf"
    dest_file: "NotoSansManichaean-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-sans-manichaean.yaml"
}
is_noto: true
languages: "aii_Mani"
languages: "xmn_Mani"
primary_script: "Mani"
