name: "Libre Baskerville"
designer: "Impallari Type"
license: "OFL"
category: "SERIF"
date_added: "2012-11-30"
fonts {
  name: "Libre Baskerville"
  style: "normal"
  weight: 400
  filename: "LibreBaskerville[wght].ttf"
  post_script_name: "LibreBaskerville-Regular"
  full_name: "Libre Baskerville Regular"
  copyright: "Copyright 2012 The Libre Baskerville Project Authors (https://github.com/impallari/Libre-Baskerville)"
}
fonts {
  name: "Libre Baskerville"
  style: "italic"
  weight: 400
  filename: "LibreBaskerville-Italic[wght].ttf"
  post_script_name: "LibreBaskerville-Italic"
  full_name: "Libre Baskerville Italic"
  copyright: "Copyright 2012 The Libre Baskerville Project Authors (https://github.com/impallari/Libre-Baskerville)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/impallari/Libre-Baskerville"
  commit: "d20160cfa0ac4c532327f85b3ca4054acf92ed38"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/variable/LibreBaskerville[wght].ttf"
    dest_file: "LibreBaskerville[wght].ttf"
  }
  files {
    source_file: "fonts/variable/LibreBaskerville-Italic[wght].ttf"
    dest_file: "LibreBaskerville-Italic[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
