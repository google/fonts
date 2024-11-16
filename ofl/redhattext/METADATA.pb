name: "Red Hat Text"
designer: "MCKL"
license: "OFL"
category: "SANS_SERIF"
date_added: "2019-04-10"
fonts {
  name: "Red Hat Text"
  style: "normal"
  weight: 400
  filename: "RedHatText[wght].ttf"
  post_script_name: "RedHatText-Light"
  full_name: "Red Hat Text Light"
  copyright: "Copyright 2021 The Red Hat Project Authors (https://github.com/RedHatOfficial/RedHatFont)"
}
fonts {
  name: "Red Hat Text"
  style: "italic"
  weight: 400
  filename: "RedHatText-Italic[wght].ttf"
  post_script_name: "RedHatText-LightItalic"
  full_name: "Red Hat Text Light Italic"
  copyright: "Copyright 2021 The Red Hat Project Authors (https://github.com/RedHatOfficial/RedHatFont)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/jeremymickel/RedHatFonts"
  commit: "d20968c93b62cedcc5ca4d2de2d8063c7efe35d1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/proportional/RedHatText[wght].ttf"
    dest_file: "RedHatText[wght].ttf"
  }
  files {
    source_file: "fonts/proportional/RedHatText-Italic[wght].ttf"
    dest_file: "RedHatText-Italic[wght].ttf"
  }
  branch: "master"
}
