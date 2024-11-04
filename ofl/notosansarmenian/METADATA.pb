name: "Noto Sans Armenian"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Armenian"
  style: "normal"
  weight: 400
  filename: "NotoSansArmenian[wdth,wght].ttf"
  post_script_name: "NotoSansArmenian-Regular"
  full_name: "Noto Sans Armenian Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/armenian)"
}
subsets: "armenian"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wdth"
  min_value: 62.5
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/armenian"
  archive_url: "https://github.com/notofonts/armenian/releases/download/NotoSansArmenian-v2.008/NotoSansArmenian-v2.008.zip"
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
    source_file: "NotoSansArmenian/googlefonts/variable/NotoSansArmenian[wdth,wght].ttf"
    dest_file: "NotoSansArmenian[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "hy_Armn"  # Armenian
languages: "hyw_Armn"  # Western Armenian, Armenian
primary_script: "Armn"
