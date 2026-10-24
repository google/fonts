name: "Gemunu Libre"
designer: "Mooniak"
license: "OFL"
category: "SANS_SERIF"
date_added: "2017-05-29"
fonts {
  name: "Gemunu Libre"
  style: "normal"
  weight: 400
  filename: "GemunuLibre[wght].ttf"
  post_script_name: "GemunuLibre-ExtraLight"
  full_name: "Gemunu Libre ExtraLight"
  copyright: "Copyright 2021 The Gemunu Libre Project Authors (https://github.com/mooniak/gemunu-libre-font/)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "sinhala"
axes {
  tag: "wght"
  min_value: 200.0
  max_value: 800.0
}
source {
  repository_url: "https://github.com/mooniak/gemunu-libre-font"
  commit: "8a8867dd893adb9e82baef9d85ccbc3764a55b0c"
  config_yaml: "sources/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/GemunuLibre[wght].ttf"
    dest_file: "GemunuLibre[wght].ttf"
  }
  branch: "main"
}
primary_script: "Sinh"
stroke: "SANS_SERIF"
classifications: "DISPLAY"
