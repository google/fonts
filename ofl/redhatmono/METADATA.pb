name: "Red Hat Mono"
designer: "MCKL"
license: "OFL"
category: "SANS_SERIF"
category: "MONOSPACE"
date_added: "2021-06-10"
fonts {
  name: "Red Hat Mono"
  style: "normal"
  weight: 400
  filename: "RedHatMono[wght].ttf"
  post_script_name: "RedHatMono-Light"
  full_name: "Red Hat Mono Light"
  copyright: "Copyright 2021 The Red Hat Project Authors (https://github.com/RedHatOfficial/RedHatFont)"
}
fonts {
  name: "Red Hat Mono"
  style: "italic"
  weight: 400
  filename: "RedHatMono-Italic[wght].ttf"
  post_script_name: "RedHatMono-LightItalic"
  full_name: "Red Hat Mono Light Italic"
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
    source_file: "fonts/mono/RedHatMono[wght].ttf"
    dest_file: "RedHatMono[wght].ttf"
  }
  files {
    source_file: "fonts/mono/RedHatMono-Italic[wght].ttf"
    dest_file: "RedHatMono-Italic[wght].ttf"
  }
  branch: "master"
}
