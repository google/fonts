name: "Kumbh Sans"
designer: "Saurabh Sharma"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-07-23"
fonts {
  name: "Kumbh Sans"
  style: "normal"
  weight: 400
  filename: "KumbhSans[YOPQ,wght].ttf"
  post_script_name: "KumbhSans-Regular"
  full_name: "Kumbh Sans Regular"
  copyright: "Copyright 2020 The KumbhSans Project Authors (https://github.com/xconsau/KumbhSans)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "symbols"
axes {
  tag: "YOPQ"
  min_value: 40.0
  max_value: 300.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
registry_default_overrides {
  key: "YOPQ"
  value: 300.0
}
source {
  repository_url: "https://github.com/xconsau/KumbhSans"
  commit: "b1c41a8ff0916a5421bd3976c361f1980c0e7cfc"
  files {
    source_file: "fonts/variable/KumbhSans[YOPQ,wght].ttf"
    dest_file: "KumbhSans[YOPQ,wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
}
