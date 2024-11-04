name: "Cuprum"
designer: "Jovanny Lemonad"
license: "OFL"
category: "SANS_SERIF"
date_added: "2012-04-04"
fonts {
  name: "Cuprum"
  style: "normal"
  weight: 400
  filename: "Cuprum[wght].ttf"
  post_script_name: "Cuprum-Regular"
  full_name: "Cuprum Regular"
  copyright: "Copyright 2020 The Cuprum Project Authors (https://github.com/alexeiva/cuprum), with Reserved Font Name \"Cuprum\"."
}
fonts {
  name: "Cuprum"
  style: "italic"
  weight: 400
  filename: "Cuprum-Italic[wght].ttf"
  post_script_name: "Cuprum-Italic"
  full_name: "Cuprum Italic"
  copyright: "Copyright 2020 The Cuprum Project Authors (https://github.com/alexeiva/cuprum), with Reserved Font Name \"Cuprum\"."
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/alexeiva/cuprum"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Cuprum-Italic[wght].ttf"
    dest_file: "Cuprum-Italic[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Cuprum[wght].ttf"
    dest_file: "Cuprum[wght].ttf"
  }
  files {
    source_file: "fonts/ttf/Cuprum-Regular.ttf"
    dest_file: "static/Cuprum-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/Cuprum-Bold.ttf"
    dest_file: "static/Cuprum-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Cuprum-Italic.ttf"
    dest_file: "static/Cuprum-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/Cuprum-BoldItalic.ttf"
    dest_file: "static/Cuprum-BoldItalic.ttf"
  }
  branch: "master"
}
