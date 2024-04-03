name: "Kufam"
designer: "Original Type, Wael Morcos, Artur Schmal"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-07-14"
fonts {
  name: "Kufam"
  style: "normal"
  weight: 400
  filename: "Kufam[wght].ttf"
  post_script_name: "Kufam-Regular"
  full_name: "Kufam Regular"
  copyright: "Copyright 2019 The Kufam Project Authors (https://github.com/originaltype/kufam)"
}
fonts {
  name: "Kufam"
  style: "italic"
  weight: 400
  filename: "Kufam-Italic[wght].ttf"
  post_script_name: "Kufam-Italic"
  full_name: "Kufam Italic"
  copyright: "Copyright 2019 The Kufam Project Authors (https://github.com/originaltype/kufam)"
}
subsets: "arabic"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/originaltype/kufam"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Fonts/VF/Kufam[wght].ttf"
    dest_file: "Kufam[wght].ttf"
  }
  files {
    source_file: "Fonts/VF/Kufam-Italic[wght].ttf"
    dest_file: "Kufam-Italic[wght].ttf"
  }
  branch: "master"
}
