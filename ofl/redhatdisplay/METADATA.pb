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
  repository_url: "https://github.com/bghryct/RedHatDisplay"
  commit: "fd36df3a3ad95084fe777597ed4b5c19961b3631"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/RedHatDisplay[wght].ttf"
    dest_file: "RedHatDisplay[wght].ttf"
  }
  files {
    source_file: "fonts/variable/RedHatDisplay-Italic[wght].ttf"
    dest_file: "RedHatDisplay-Italic[wght].ttf"
  }
  branch: "main"
}

stroke: "SANS_SERIF"
classifications: "DISPLAY"
