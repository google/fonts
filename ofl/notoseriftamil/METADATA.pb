name: "Noto Serif Tamil"
designer: "Google"
license: "OFL"
category: "SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Serif Tamil"
  style: "normal"
  weight: 400
  filename: "NotoSerifTamil[wdth,wght].ttf"
  post_script_name: "NotoSerifTamil-Regular"
  full_name: "Noto Serif Tamil Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/tamil)"
}
fonts {
  name: "Noto Serif Tamil"
  style: "italic"
  weight: 400
  filename: "NotoSerifTamil-Italic[wdth,wght].ttf"
  post_script_name: "NotoSerifTamil-Italic"
  full_name: "Noto Serif Tamil Italic"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/tamil)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "tamil"
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
  repository_url: "https://github.com/notofonts/tamil"
  archive_url: "https://github.com/notofonts/tamil/releases/download/NotoSerifTamil-v2.004/NotoSerifTamil-v2.004.zip"
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
    source_file: "NotoSerifTamil/googlefonts/variable-ttf/NotoSerifTamil[wdth,wght].ttf"
    dest_file: "NotoSerifTamil[wdth,wght].ttf"
  }
  files {
    source_file: "NotoSerifTamil/googlefonts/variable-ttf/NotoSerifTamil-Italic[wdth,wght].ttf"
    dest_file: "NotoSerifTamil-Italic[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "bfq_Taml"  # Badaga
languages: "ta_Taml"  # Tamil
primary_script: "Taml"
