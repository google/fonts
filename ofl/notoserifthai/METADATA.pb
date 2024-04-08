name: "Noto Serif Thai"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Thai"
  style: "normal"
  weight: 400
  filename: "NotoSerifThai[wdth,wght].ttf"
  post_script_name: "NotoSerifThai-Regular"
  full_name: "Noto Serif Thai Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/thai)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "thai"
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
  repository_url: "https://github.com/notofonts/thai"
  archive_url: "https://github.com/notofonts/thai/releases/download/NotoSerifThai-v2.002/NotoSerifThai-v2.002.zip"
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
    source_file: "NotoSerifThai/googlefonts/variable/NotoSerifThai[wdth,wght].ttf"
    dest_file: "NotoSerifThai[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "kdt_Thai"  # Kuy
languages: "kxm_Thai"  # Northern Khmer
languages: "lcp_Thai"  # Western Lawa
languages: "lwl_Thai"  # Eastern Lawa
languages: "pi_Thai"  # Pali, Thai
languages: "sou_Thai"  # Southern Thai
languages: "th_Thai"  # Thai
languages: "tts_Thai"  # Northeastern Thai
primary_script: "Thai"
