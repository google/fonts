name: "Mulish"
designer: "Vernon Adams, Cyreal, Jacques Le Bailly"
license: "OFL"
category: "SANS_SERIF"
date_added: "2011-05-25"
fonts {
  name: "Mulish"
  style: "normal"
  weight: 400
  filename: "Mulish[wght].ttf"
  post_script_name: "Mulish-ExtraLight"
  full_name: "Mulish ExtraLight"
  copyright: "Copyright 2016 The Mulish Project Authors (https://github.com/googlefonts/mulish)"
}
fonts {
  name: "Mulish"
  style: "italic"
  weight: 400
  filename: "Mulish-Italic[wght].ttf"
  post_script_name: "Mulish-ExtraLightItalic"
  full_name: "Mulish ExtraLight Italic"
  copyright: "Copyright 2016 The Mulish Project Authors (https://github.com/googlefonts/mulish)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 200.0
  max_value: 1000.0
}
source {
  repository_url: "https://github.com/googlefonts/mulish"
  files {
    source_file: "fonts/variable/Mulish[wght].ttf"
    dest_file: "Mulish[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Mulish-Italic[wght].ttf"
    dest_file: "Mulish-Italic[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
}
