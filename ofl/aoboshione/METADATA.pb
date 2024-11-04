name: "Aoboshi One"
designer: "Natsumi Matsuba"
license: "OFL"
category: "SERIF"
date_added: "2020-12-16"
fonts {
  name: "Aoboshi One"
  style: "normal"
  weight: 400
  filename: "AoboshiOne-Regular.ttf"
  post_script_name: "AoboshiOne-Regular"
  full_name: "Aoboshi One Regular"
  copyright: "Copyright 2020 The Aoboshi Font Project Authors (https://github.com/matsuba723/Aoboshi), all rights reserved."
}
subsets: "japanese"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/matsuba723/Aoboshi"
  files {
    source_file: "fonts/ttf/AoboshiOne-Regular.ttf"
    dest_file: "AoboshiOne-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
languages: "ja_Kana"  # Japanese, Katakana
languages: "ja_Hira"  # Japanese, Hiragana
primary_script: "Hira"
