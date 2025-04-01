name: "Comic Relief"
designer: "Jeff Davis"
license: "OFL"
category: "DISPLAY"
date_added: "2025-02-13"
fonts {
  name: "Comic Relief"
  style: "normal"
  weight: 400
  filename: "ComicRelief-Regular.ttf"
  post_script_name: "ComicRelief-Regular"
  full_name: "Comic Relief Regular"
  copyright: "Copyright 2013 The Comic Relief Project Authors (https://github.com/loudifier/Comic-Relief)"
}
fonts {
  name: "Comic Relief"
  style: "normal"
  weight: 700
  filename: "ComicRelief-Bold.ttf"
  post_script_name: "ComicRelief-Bold"
  full_name: "Comic Relief Bold"
  copyright: "Copyright 2013 The Comic Relief Project Authors (https://github.com/loudifier/Comic-Relief)"
}
subsets: "cyrillic"
subsets: "greek"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/loudifier/Comic-Relief"
  commit: "856315f5a45dfdad75090e4454f1ebfd019296b9"
  archive_url: "https://github.com/loudifier/Comic-Relief/releases/download/v1.2/Comic-Relief-v1.2.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/ComicRelief-Regular.ttf"
    dest_file: "ComicRelief-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/ComicRelief-Bold.ttf"
    dest_file: "ComicRelief-Bold.ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
