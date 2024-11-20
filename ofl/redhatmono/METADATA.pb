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
  post_script_name: "RedHatMono-Regular"
  full_name: "Red Hat Mono Regular"
  copyright: "Copyright 2024 The Red Hat Project Authors (https://github.com/RedHatOfficial/RedHatFont)"
}
fonts {
  name: "Red Hat Mono"
  style: "italic"
  weight: 400
  filename: "RedHatMono-Italic[wght].ttf"
  post_script_name: "RedHatMono-Italic"
  full_name: "Red Hat Mono Italic"
  copyright: "Copyright 2024 The Red Hat Project Authors (https://github.com/RedHatOfficial/RedHatFont)"
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
  repository_url: "https://github.com/bghryct/RedHatMono"
  commit: "a0f2a7032143500e44dfd569d09ba30414d51a1c"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/RedHatMono[wght].ttf"
    dest_file: "RedHatMono[wght].ttf"
  }
  files {
    source_file: "fonts/variable/RedHatMono-Italic[wght].ttf"
    dest_file: "RedHatMono-Italic[wght].ttf"
  }
  branch: "main"
}

classifications: "MONOSPACE"
stroke: "SANS_SERIF"
