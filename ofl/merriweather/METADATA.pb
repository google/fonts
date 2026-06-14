name: "Merriweather"
designer: "Sorkin Type"
license: "OFL"
category: "SERIF"
date_added: "2011-05-11"
fonts {
  name: "Merriweather"
  style: "normal"
  weight: 400
  filename: "Merriweather[opsz,wdth,wght].ttf"
  post_script_name: "Merriweather-Light"
  full_name: "Merriweather Light"
  copyright: "Copyright 2024 The Merriweather Project Authors (https://github.com/EbenSorkin/Merriweather4) with Reserved Font Name \"Merriweather\"."
}
fonts {
  name: "Merriweather"
  style: "italic"
  weight: 400
  filename: "Merriweather-Italic[opsz,wdth,wght].ttf"
  post_script_name: "Merriweather-LightItalic"
  full_name: "Merriweather Light Italic"
  copyright: "Copyright 2024 The Merriweather Project Authors (https://github.com/EbenSorkin/Merriweather4) with Reserved Font Name \"Merriweather\"."
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "opsz"
  min_value: 18.0
  max_value: 144.0
}
axes {
  tag: "wdth"
  min_value: 87.0
  max_value: 112.0
}
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 900.0
}
registry_default_overrides {
  key: "opsz"
  value: 18.0
}
source {
  repository_url: "https://github.com/EbenSorkin/Merriweather4"
  commit: "e586023aa0fe1dba9a7d4ec80fa8b9e546cb7ecf"
  archive_url: "https://github.com/EbenSorkin/Merriweather4/releases/download/4.008/Merriweather4-4.008.zip"
  files {
    source_file: "fonts/variable/Merriweather[opsz,wdth,wght].ttf"
    dest_file: "Merriweather[opsz,wdth,wght].ttf"
  }
  files {
    source_file: "fonts/variable/Merriweather-Italic[opsz,wdth,wght].ttf"
    dest_file: "Merriweather-Italic[opsz,wdth,wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 300.0
    max_value: 300.0
  }
  axis_target {
    tag: "wdth"
    min_value: 100.0
    max_value: 100.0
  }
  axis_target {
    tag: "opsz"
    min_value: 18.0
    max_value: 18.0
  }
  axis_target {
    tag: "ital"
    min_value: 0.0
    max_value: 0.0
  }
  target {
    target_type: TARGET_OS_ANDROID
  }
  size_adjust_pct: 109.38
  local_src: "Roboto"
  ascent_override_pct: 90.63
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 400.0
    max_value: 400.0
  }
  axis_target {
    tag: "wdth"
    min_value: 100.0
    max_value: 100.0
  }
  axis_target {
    tag: "opsz"
    min_value: 18.0
    max_value: 18.0
  }
  axis_target {
    tag: "ital"
    min_value: 0.0
    max_value: 0.0
  }
  target {
    target_type: TARGET_OS_ANDROID
  }
  size_adjust_pct: 109.77
  local_src: "Roboto"
  ascent_override_pct: 90.63
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 700.0
    max_value: 700.0
  }
  axis_target {
    tag: "wdth"
    min_value: 100.0
    max_value: 100.0
  }
  axis_target {
    tag: "opsz"
    min_value: 18.0
    max_value: 18.0
  }
  axis_target {
    tag: "ital"
    min_value: 0.0
    max_value: 0.0
  }
  target {
    target_type: TARGET_OS_ANDROID
  }
  size_adjust_pct: 112.3
  local_src: "Roboto"
  ascent_override_pct: 87.5
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 900.0
    max_value: 900.0
  }
  axis_target {
    tag: "wdth"
    min_value: 100.0
    max_value: 100.0
  }
  axis_target {
    tag: "opsz"
    min_value: 18.0
    max_value: 18.0
  }
  axis_target {
    tag: "ital"
    min_value: 0.0
    max_value: 0.0
  }
  target {
    target_type: TARGET_OS_ANDROID
  }
  size_adjust_pct: 114.06
  local_src: "Roboto"
  ascent_override_pct: 85.94
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 300.0
    max_value: 300.0
  }
  axis_target {
    tag: "wdth"
    min_value: 100.0
    max_value: 100.0
  }
  axis_target {
    tag: "opsz"
    min_value: 18.0
    max_value: 18.0
  }
  axis_target {
    tag: "ital"
    min_value: 1.0
    max_value: 1.0
  }
  target {
    target_type: TARGET_OS_ANDROID
  }
  size_adjust_pct: 105.08
  local_src: "Roboto Italic"
  ascent_override_pct: 95.31
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 400.0
    max_value: 400.0
  }
  axis_target {
    tag: "wdth"
    min_value: 100.0
    max_value: 100.0
  }
  axis_target {
    tag: "opsz"
    min_value: 18.0
    max_value: 18.0
  }
  axis_target {
    tag: "ital"
    min_value: 1.0
    max_value: 1.0
  }
  target {
    target_type: TARGET_OS_ANDROID
  }
  size_adjust_pct: 109.38
  local_src: "Roboto Italic"
  ascent_override_pct: 90.63
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 700.0
    max_value: 700.0
  }
  axis_target {
    tag: "wdth"
    min_value: 100.0
    max_value: 100.0
  }
  axis_target {
    tag: "opsz"
    min_value: 18.0
    max_value: 18.0
  }
  axis_target {
    tag: "ital"
    min_value: 1.0
    max_value: 1.0
  }
  target {
    target_type: TARGET_OS_ANDROID
  }
  size_adjust_pct: 108.2
  local_src: "Roboto Italic"
  ascent_override_pct: 90.63
}
fallbacks {
  axis_target {
    tag: "wght"
    min_value: 900.0
    max_value: 900.0
  }
  axis_target {
    tag: "wdth"
    min_value: 100.0
    max_value: 100.0
  }
  axis_target {
    tag: "opsz"
    min_value: 18.0
    max_value: 18.0
  }
  axis_target {
    tag: "ital"
    min_value: 1.0
    max_value: 1.0
  }
  target {
    target_type: TARGET_OS_ANDROID
  }
  size_adjust_pct: 112.5
  local_src: "Roboto Italic"
  ascent_override_pct: 87.5
}
