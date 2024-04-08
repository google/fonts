name: "Schibsted Grotesk"
designer: "Bakken & Bæck, Henrik Kongsvoll"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-03-03"
fonts {
  name: "Schibsted Grotesk"
  style: "normal"
  weight: 400
  filename: "SchibstedGrotesk[wght].ttf"
  post_script_name: "SchibstedGrotesk-Regular"
  full_name: "Schibsted Grotesk Regular"
  copyright: "Copyright 2023 The Schibsted-Grotesk Project Authors (https://github.com/schibsted/schibsted-grotesk)"
}
fonts {
  name: "Schibsted Grotesk"
  style: "italic"
  weight: 400
  filename: "SchibstedGrotesk-Italic[wght].ttf"
  post_script_name: "SchibstedGrotesk-Italic"
  full_name: "Schibsted Grotesk Italic"
  copyright: "Copyright 2023 The Schibsted-Grotesk Project Authors (https://github.com/schibsted/schibsted-grotesk)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/schibsted/schibsted-grotesk"
  commit: "d485f61f105e1b3935f4d21dfb4d371359798603"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/SchibstedGrotesk[wght].ttf"
    dest_file: "SchibstedGrotesk[wght].ttf"
  }
  files {
    source_file: "fonts/variable/SchibstedGrotesk-Italic[wght].ttf"
    dest_file: "SchibstedGrotesk-Italic[wght].ttf"
  }
  branch: "main"
}
