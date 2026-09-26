name: "Cormorant Garamond"
designer: "Christian Thalmann"
license: "OFL"
category: "SERIF"
date_added: "2017-01-18"
fonts {
  name: "Cormorant Garamond"
  style: "normal"
  weight: 400
  filename: "CormorantGaramond[wght].ttf"
  post_script_name: "CormorantGaramond-Light"
  full_name: "Cormorant Garamond Light"
  copyright: "Copyright 2015 The Cormorant Project Authors (github.com/CatharsisFonts/Cormorant)"
}
fonts {
  name: "Cormorant Garamond"
  style: "italic"
  weight: 400
  filename: "CormorantGaramond-Italic[wght].ttf"
  post_script_name: "CormorantGaramond-LightItalic"
  full_name: "Cormorant Garamond Light Italic"
  copyright: "Copyright 2015 The Cormorant Project Authors (github.com/CatharsisFonts/Cormorant)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/CatharsisFonts/Cormorant"
  commit: "6d210fd3550b7358ca62d6ba3e354ec1ec940813"
  config_yaml: "sources/config-garamond.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/CormorantGaramond[wght].ttf"
    dest_file: "CormorantGaramond[wght].ttf"
  }
  files {
    source_file: "fonts/variable/CormorantGaramond-Italic[wght].ttf"
    dest_file: "CormorantGaramond-Italic[wght].ttf"
  }
  branch: "master"
}
