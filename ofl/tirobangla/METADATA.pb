name: "Tiro Bangla"
designer: "Tiro Typeworks, John Hudson, Fiona Ross, Neelakash Kshetrimayum"
license: "OFL"
category: "SERIF"
date_added: "2022-03-30"
fonts {
  name: "Tiro Bangla"
  style: "normal"
  weight: 400
  filename: "TiroBangla-Regular.ttf"
  post_script_name: "TiroBangla-Regular"
  full_name: "Tiro Bangla Regular"
  copyright: "Copyright 2020 The Indigo Project Authors (https://github.com/TiroTypeworks/Indigo)"
}
fonts {
  name: "Tiro Bangla"
  style: "italic"
  weight: 400
  filename: "TiroBangla-Italic.ttf"
  post_script_name: "TiroBangla-Italic"
  full_name: "Tiro Bangla Italic"
  copyright: "Copyright 2020 The Indigo Project Authors (https://github.com/TiroTypeworks/Indigo)"
}
subsets: "bengali"
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
    source_file: "docs/descriptions/TiroBangla/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/TiroBangla/TTF/TiroBangla-Regular.ttf"
    dest_file: "TiroBangla-Regular.ttf"
  }
  files {
    source_file: "fonts/TiroBangla/TTF/TiroBangla-Italic.ttf"
    dest_file: "TiroBangla-Italic.ttf"
  }
  branch: "main"
}
primary_script: "Beng"
