name: "Public Sans"
designer: "USWDS, Dan Williams, Pablo Impallari, Rodrigo Fuenzalida"
license: "OFL"
category: "SANS_SERIF"
date_added: "2019-06-07"
fonts {
  name: "Public Sans"
  style: "normal"
  weight: 400
  filename: "PublicSans[wght].ttf"
  post_script_name: "PublicSans-Thin"
  full_name: "Public Sans Thin"
  copyright: "Copyright 2015 The Public Sans Project Authors (https://github.com/uswds/public-sans)"
}
fonts {
  name: "Public Sans"
  style: "italic"
  weight: 400
  filename: "PublicSans-Italic[wght].ttf"
  post_script_name: "PublicSans-ThinItalic"
  full_name: "Public Sans Thin Italic"
  copyright: "Copyright 2015 The Public Sans Project Authors (https://github.com/uswds/public-sans)"
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
  repository_url: "https://github.com/uswds/public-sans"
  commit: "c7923167a592d941646f99fb7b5fba17aa7d69e1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/PublicSans[wght].ttf"
    dest_file: "PublicSans[wght].ttf"
  }
  files {
    source_file: "fonts/variable/PublicSans-Italic[wght].ttf"
    dest_file: "PublicSans-Italic[wght].ttf"
  }
  branch: "main"
}
minisite_url: "https://public-sans.digital.gov/"
