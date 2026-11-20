name: "Cal Sans"
designer: "Mark Davis, Cal.com Inc."
license: "OFL"
category: "SANS_SERIF"
date_added: "2025-03-19"
fonts {
  name: "Cal Sans"
  style: "normal"
  weight: 400
  filename: "CalSans[GEOM,SHRP,YTAS,opsz,wght].ttf"
  post_script_name: "CalSans-Regular"
  full_name: "Cal Sans Regular"
  copyright: "Copyright 2021 The Cal Sans Project Authors (https://github.com/calcom/sans)"
}
fonts {
  name: "Cal Sans"
  style: "italic"
  weight: 400
  filename: "CalSans-Italic[GEOM,SHRP,YTAS,opsz,wght].ttf"
  post_script_name: "CalSans-Italic"
  full_name: "Cal Sans Italic"
  copyright: "Copyright 2021 The Cal Sans Project Authors (https://github.com/calcom/sans)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "GEOM"
  min_value: 0.0
  max_value: 100.0
}
axes {
  tag: "SHRP"
  min_value: 0.0
  max_value: 100.0
}
axes {
  tag: "YTAS"
  min_value: 720.0
  max_value: 800.0
}
axes {
  tag: "opsz"
  min_value: 8.0
  max_value: 48.0
}
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/calcom/sans"
  commit: "7529124c86c5f94f57f95455b87f5104fc2295c2"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/calsans-google-fonts/variable/CalSans[GEOM,SHRP,YTAS,opsz,wght].ttf"
    dest_file: "CalSans[GEOM,SHRP,YTAS,opsz,wght].ttf"
  }
  files {
    source_file: "fonts/calsans-google-fonts/variable/CalSans-Italic[GEOM,SHRP,YTAS,opsz,wght].ttf"
    dest_file: "CalSans-Italic[GEOM,SHRP,YTAS,opsz,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
stroke: "SANS_SERIF"
