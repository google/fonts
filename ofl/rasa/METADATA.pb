name: "Rasa"
designer: "Rosetta, Anna Giedryś, David Březina"
license: "OFL"
category: "SERIF"
date_added: "2016-06-20"
fonts {
  name: "Rasa"
  style: "normal"
  weight: 400
  filename: "Rasa[wght].ttf"
  post_script_name: "Rasa-Regular"
  full_name: "Rasa Regular"
  copyright: "Copyright 2015 The Yrsa-Rasa Project Authors (https://github.com/rosettatype/yrsa-rasa/)"
}
fonts {
  name: "Rasa"
  style: "italic"
  weight: 400
  filename: "Rasa-Italic[wght].ttf"
  post_script_name: "Rasa-Italic"
  full_name: "Rasa Italic"
  copyright: "Copyright 2015 The Yrsa-Rasa Project Authors (https://github.com/rosettatype/yrsa-rasa/)"
}
subsets: "gujarati"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/rosettatype/yrsa-rasa"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/Rasa-DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/RasaVariable/RasaVF-Ups.ttf"
    dest_file: "Rasa[wght].ttf"
  }
  files {
    source_file: "fonts/RasaVariable/RasaVF-Its.ttf"
    dest_file: "Rasa-Italic[wght].ttf"
  }
  branch: "master"
}
stroke: "SERIF"
classifications: "DISPLAY"
