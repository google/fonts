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
  post_script_name: "RedHatText-Regular"
  full_name: "Red Hat Text Regular"
  copyright: "Copyright 2024 The Red Hat Project Authors (https://github.com/RedHatOfficial/RedHatFont)"
}
fonts {
  name: "Red Hat Text"
  style: "italic"
  weight: 400
  filename: "RedHatText-Italic[wght].ttf"
  post_script_name: "RedHatText-Italic"
  full_name: "Red Hat Text Italic"
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
  repository_url: "https://github.com/RedHatOfficial/RedHatFont"
  commit: "32287097803f6c58136b60bc7a4a594a7fcbd689"
  config_yaml: "source/Proportional/RedHatText/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Proportional/RedHatText/variable/RedHatText[wght].ttf"
    dest_file: "RedHatText[wght].ttf"
  }
  files {
    source_file: "fonts/Proportional/RedHatText/variable/RedHatText-Italic[wght].ttf"
    dest_file: "RedHatText-Italic[wght].ttf"
  }
  branch: "master"
}

stroke: "SANS_SERIF"
