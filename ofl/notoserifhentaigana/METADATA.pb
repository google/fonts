name: "Noto Serif Hentaigana"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2024-02-26"
fonts {
  name: "Noto Serif Hentaigana"
  style: "normal"
  weight: 400
  filename: "NotoSerifHentaigana[wght].ttf"
  post_script_name: "NotoSerifHentaigana-ExtraLight"
  full_name: "Noto Serif Hentaigana ExtraLight"
  copyright: "Copyright 2023 The Noto Project Authors (https://github.com/notofonts/hentaigana)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 200.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/hentaigana"
  archive_url: "https://github.com/notofonts/hentaigana/releases/download/NotoSerifHentaigana-v1.000/NotoSerifHentaigana-v1.000.zip"
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
    source_file: "NotoSerifHentaigana/googlefonts/variable/NotoSerifHentaigana[wght].ttf"
    dest_file: "NotoSerifHentaigana[wght].ttf"
  }
  branch: "main"
}
is_noto: true
primary_script: "Hira"
