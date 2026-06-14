name: "Baskervville"
designer: "ANRT"
license: "OFL"
category: "SERIF"
date_added: "2019-10-04"
fonts {
  name: "Baskervville"
  style: "normal"
  weight: 400
  filename: "Baskervville[wght].ttf"
  post_script_name: "Baskervville-Regular"
  full_name: "Baskervville Regular"
  copyright: "Copyright 2018 The Baskervville Project Authors (https://github.com/anrt-type/ANRT-Baskervville)"
}
fonts {
  name: "Baskervville"
  style: "italic"
  weight: 400
  filename: "Baskervville-Italic[wght].ttf"
  post_script_name: "Baskervville-Italic"
  full_name: "Baskervville Italic"
  copyright: "Copyright 2018 The Baskervville Project Authors (https://github.com/anrt-type/ANRT-Baskervville)"
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
  repository_url: "https://github.com/anrt-type/ANRT-Baskervville"
  commit: "0629447774568fd957d98736487afb000be38b55"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Baskervville[wght].ttf"
    dest_file: "Baskervville[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Baskervville-Italic[wght].ttf"
    dest_file: "Baskervville-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
