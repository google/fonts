name: "Instrument Serif"
designer: "Rodrigo Fuenzalida, Jordan Egstad"
license: "OFL"
category: "SERIF"
date_added: "2023-03-22"
fonts {
  name: "Instrument Serif"
  style: "normal"
  weight: 400
  filename: "InstrumentSerif-Regular.ttf"
  post_script_name: "InstrumentSerif-Regular"
  full_name: "Instrument Serif Regular"
  copyright: "Copyright 2022 The Instrument Serif Project Authors (https://github.com/Instrument/instrument-serif)"
}
fonts {
  name: "Instrument Serif"
  style: "italic"
  weight: 400
  filename: "InstrumentSerif-Italic.ttf"
  post_script_name: "InstrumentSerif-Italic"
  full_name: "Instrument Serif Italic"
  copyright: "Copyright 2022 The Instrument Serif Project Authors (https://github.com/Instrument/instrument-serif)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/Instrument/instrument-serif"
  commit: "65c0ef225f386a3c7e87570a4aa9cc0262c2fd81"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/InstrumentSerif-Regular.ttf"
    dest_file: "InstrumentSerif-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/InstrumentSerif-Italic.ttf"
    dest_file: "InstrumentSerif-Italic.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
