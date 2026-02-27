name: "Red Hat Display"
designer: "MCKL"
license: "OFL"
category: "SANS_SERIF"
date_added: "2019-04-10"
fonts {
  name: "Red Hat Display"
  style: "normal"
  weight: 400
  filename: "RedHatDisplay[wght].ttf"
  post_script_name: "RedHatDisplay-Regular"
  full_name: "Red Hat Display Regular"
  copyright: "Copyright 2024 The Red Hat Project Authors (https://github.com/RedHatOfficial/RedHatFont)"
}
fonts {
  name: "Red Hat Display"
  style: "italic"
  weight: 400
  filename: "RedHatDisplay-Italic[wght].ttf"
  post_script_name: "RedHatDisplay-Italic"
  full_name: "Red Hat Display Italic"
  copyright: "Copyright 2024 The Red Hat Project Authors (https://github.com/RedHatOfficial/RedHatFont)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/RedHatOfficial/RedHatFont"
  commit: "32287097803f6c58136b60bc7a4a594a7fcbd689"
  config_yaml: "source/Proportional/RedHatDisplay/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Proportional/RedHatDisplay/variable/RedHatDisplay[wght].ttf"
    dest_file: "RedHatDisplay[wght].ttf"
  }
  files {
    source_file: "fonts/Proportional/RedHatDisplay/variable/RedHatDisplay-Italic[wght].ttf"
    dest_file: "RedHatDisplay-Italic[wght].ttf"
  }
  branch: "master"
}

stroke: "SANS_SERIF"
classifications: "DISPLAY"
