name: "Hanken Grotesk"
designer: "Alfredo Marco Pradil, Hanken Design Co."
license: "OFL"
category: "SANS_SERIF"
date_added: "2022-11-16"
fonts {
  name: "Hanken Grotesk"
  style: "normal"
  weight: 400
  filename: "HankenGrotesk[wght].ttf"
  post_script_name: "HankenGrotesk-Regular"
  full_name: "Hanken Grotesk Regular"
  copyright: "Copyright 2021 The Hanken Grotesk Project Authors (https://github.com/marcologous/hanken-grotesk)"
}
fonts {
  name: "Hanken Grotesk"
  style: "italic"
  weight: 400
  filename: "HankenGrotesk-Italic[wght].ttf"
  post_script_name: "HankenGrotesk-Italic"
  full_name: "Hanken Grotesk Italic"
  copyright: "Copyright 2021 The Hanken Grotesk Project Authors (https://github.com/marcologous/hanken-grotesk)"
}
subsets: "cyrillic-ext"
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
  repository_url: "https://github.com/marcologous/hanken-grotesk"
  commit: "e6e3c4df55acfe44333c587e3d97ae3c44b7dce5"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/HankenGrotesk[wght].ttf"
    dest_file: "HankenGrotesk[wght].ttf"
  }
  files {
    source_file: "fonts/variable/HankenGrotesk-Italic[wght].ttf"
    dest_file: "HankenGrotesk-Italic[wght].ttf"
  }
  branch: "master"
}
