name: "REM"
designer: "Octavio Pardo"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-06-30"
fonts {
  name: "REM"
  style: "normal"
  weight: 400
  filename: "REM[wght].ttf"
  post_script_name: "REM-Medium"
  full_name: "REM Medium"
  copyright: "Copyright 2019 The REM Project Authors (https://github.com/octaviopardo/REM)"
}
fonts {
  name: "REM"
  style: "italic"
  weight: 400
  filename: "REM-Italic[wght].ttf"
  post_script_name: "REM-MediumItalic"
  full_name: "REM Medium Italic"
  copyright: "Copyright 2019 The REM Project Authors (https://github.com/octaviopardo/REM)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/octaviopardo/REM"
  commit: "b26d584ebdb3d8084355205d22c87e4e99658d56"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/REM[wght].ttf"
    dest_file: "REM[wght].ttf"
  }
  files {
    source_file: "fonts/variable/REM-Italic[wght].ttf"
    dest_file: "REM-Italic[wght].ttf"
  }
  branch: "master"
}
