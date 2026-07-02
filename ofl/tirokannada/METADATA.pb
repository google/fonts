name: "Tiro Kannada"
designer: "Tiro Typeworks, John Hudson, Fiona Ross, Kaja Słojewska"
license: "OFL"
category: "SERIF"
date_added: "2022-03-30"
fonts {
  name: "Tiro Kannada"
  style: "normal"
  weight: 400
  filename: "TiroKannada-Regular.ttf"
  post_script_name: "TiroKannada-Regular"
  full_name: "Tiro Kannada Regular"
  copyright: "Copyright 2020 The Indigo Project Authors (https://github.com/TiroTypeworks/Indigo)"
}
fonts {
  name: "Tiro Kannada"
  style: "italic"
  weight: 400
  filename: "TiroKannada-Italic.ttf"
  post_script_name: "TiroKannada-Italic"
  full_name: "Tiro Kannada Italic"
  copyright: "Copyright 2020 The Indigo Project Authors (https://github.com/TiroTypeworks/Indigo)"
}
subsets: "kannada"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/TiroTypeworks/Indigo"
  commit: "98b5d3a01c534b7029af04a59d31e0d7d90be15a"
  files {
    source_file: "fonts/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "docs/descriptions/TiroKannada/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/TiroKannada/TTF/TiroKannada-Regular.ttf"
    dest_file: "TiroKannada-Regular.ttf"
  }
  files {
    source_file: "fonts/TiroKannada/TTF/TiroKannada-Italic.ttf"
    dest_file: "TiroKannada-Italic.ttf"
  }
  branch: "main"
}
primary_script: "Knda"
