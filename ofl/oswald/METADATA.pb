name: "Oswald"
designer: "Vernon Adams, Kalapi Gajjar, Cyreal"
license: "OFL"
category: "SANS_SERIF"
date_added: "2012-02-29"
fonts {
  name: "Oswald"
  style: "normal"
  weight: 400
  filename: "Oswald[wght].ttf"
  post_script_name: "Oswald-Regular"
  full_name: "Oswald Regular"
  copyright: "Copyright 2016 The Oswald Project Authors (https://github.com/googlefonts/OswaldFont)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 200.0
  max_value: 700.0
}

fallbacks {
  axis_target {
    tag: "wght"
    min_value: 200
    max_value: 200
  }
  target {
    target_type: TARGET_OS_MAC
  }
  size_adjust_pct: 85.94
  ascent_override_pct: 175
  local_src: "Impact"
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 300
    max_value: 300
  }
  target {
    target_type: TARGET_OS_MAC
  }
  size_adjust_pct: 87.5
  ascent_override_pct: 137.5
  local_src: "Impact"
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 400
    max_value: 400
  }
  target {
    target_type: TARGET_OS_MAC
  }
  size_adjust_pct: 91.41
  ascent_override_pct: 141.41
  local_src: "Impact"
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 500
    max_value: 500
  }
  target {
    target_type: TARGET_OS_MAC
  }
  size_adjust_pct: 93.75
  ascent_override_pct: 137.5
  local_src: "Impact"
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 600
    max_value: 600
  }
  target {
    target_type: TARGET_OS_MAC
  }
  size_adjust_pct: 99.61
  ascent_override_pct: 128.13
  local_src: "Impact"
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 700
    max_value: 700
  }
  target {
    target_type: TARGET_OS_MAC
  }
  size_adjust_pct: 100.78
  ascent_override_pct: 125
  local_src: "Impact"
}
