name: "Noto Serif Telugu"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Telugu"
  style: "normal"
  weight: 400
  filename: "NotoSerifTelugu[wght].ttf"
  post_script_name: "NotoSerifTelugu-Regular"
  full_name: "Noto Serif Telugu Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/telugu)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "telugu"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/notofonts/telugu"
  archive_url: "https://github.com/notofonts/telugu/releases/download/NotoSerifTelugu-v2.005/NotoSerifTelugu-v2.005.zip"
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
    source_file: "NotoSerifTelugu/googlefonts/variable/NotoSerifTelugu[wght].ttf"
    dest_file: "NotoSerifTelugu[wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "gon_Telu"  # Gondi, Telugu
languages: "lmn_Telu"  # Lambadi
languages: "te_Telu"  # Telugu
languages: "wbq_Telu"  # Waddar
primary_script: "Telu"
