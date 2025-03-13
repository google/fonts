name: "Roboto"
designer: "Christian Robertson, ParaType, Font Bureau"
license: "OFL"
category: "SANS_SERIF"
date_added: "2013-01-09"
fonts {
  name: "Roboto"
  style: "normal"
  weight: 400
  filename: "Roboto[wdth,wght].ttf"
  post_script_name: "Roboto-Regular"
  full_name: "Roboto Regular"
  copyright: "Copyright 2011 The Roboto Project Authors (https://github.com/googlefonts/roboto-classic)"
}
fonts {
  name: "Roboto"
  style: "italic"
  weight: 400
  filename: "Roboto-Italic[wdth,wght].ttf"
  post_script_name: "Roboto-Italic"
  full_name: "Roboto Italic"
  copyright: "Copyright 2011 The Roboto Project Authors (https://github.com/googlefonts/roboto-classic)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "greek"
subsets: "greek-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "symbols"
subsets: "vietnamese"
axes {
  tag: "wdth"
  min_value: 75.0
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/googlefonts/roboto-classic"
  commit: "b3ab25297a96373a8053db2d6fbf94b3ce61a8ac"
  archive_url: "https://github.com/googlefonts/roboto-3-classic/releases/download/v3.011/Roboto_v3.011.zip"
  files {
    source_file: "web/split/Roboto[wdth,wght].ttf"
    dest_file: "Roboto[wdth,wght].ttf"
  }
  files {
    source_file: "web/split/Roboto-Italic[wdth,wght].ttf"
    dest_file: "Roboto-Italic[wdth,wght].ttf"
  }
  branch: "main"
}
