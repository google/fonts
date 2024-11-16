name: "Castoro"
designer: "Tiro Typeworks, John Hudson, Paul Hanslow, Kaja Słojewska"
license: "OFL"
category: "SERIF"
date_added: "2020-11-03"
fonts {
  name: "Castoro"
  style: "normal"
  weight: 400
  filename: "Castoro-Regular.ttf"
  post_script_name: "Castoro-Regular"
  full_name: "Castoro Regular"
  copyright: "Copyright 2020 The Castoro Project Authors (https://github.com/TiroTypeworks/Castoro)"
}
fonts {
  name: "Castoro"
  style: "italic"
  weight: 400
  filename: "Castoro-Italic.ttf"
  post_script_name: "Castoro-Italic"
  full_name: "Castoro Italic"
  copyright: "Copyright 2020 The Castoro Project Authors (https://github.com/TiroTypeworks/Castoro)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/TiroTypeworks/Castoro"
  commit: "58a386a96e522b6d47c566175c7ee799d4c8d14f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "docs/descriptions/Castoro/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/Castoro/TTF/Castoro-Regular.ttf"
    dest_file: "Castoro-Regular.ttf"
  }
  files {
    source_file: "fonts/Castoro/TTF/Castoro-Italic.ttf"
    dest_file: "Castoro-Italic.ttf"
  }
  branch: "master"
}
