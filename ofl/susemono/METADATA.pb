name: "SUSE Mono"
designer: "René Bieder"
license: "OFL"
category: "SANS_SERIF"
date_added: "2025-08-20"
fonts {
  name: "SUSE Mono"
  style: "normal"
  weight: 400
  filename: "SUSEMono[wght].ttf"
  post_script_name: "SUSEMono-Thin"
  full_name: "SUSE Mono Thin"
  copyright: "Copyright 2025 The SUSE Project Authors (https://github.com/SUSE/suse-font)"
}
fonts {
  name: "SUSE Mono"
  style: "italic"
  weight: 400
  filename: "SUSEMono-Italic[wght].ttf"
  post_script_name: "SUSEMono-ThinItalic"
  full_name: "SUSE Mono Thin Italic"
  copyright: "Copyright 2025 The SUSE Project Authors (https://github.com/SUSE/suse-font)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 800.0
}
source {
  repository_url: "https://github.com/SUSE/suse-font"
  commit: "7159afb2555b06d3a5c2f90e4d324e59e69c277d"
  archive_url: "https://github.com/SUSE/suse-font/releases/download/v2.000/suse-font-v2.000.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/SUSEMono[wght].ttf"
    dest_file: "SUSEMono[wght].ttf"
  }
  files {
    source_file: "fonts/variable/SUSEMono-Italic[wght].ttf"
    dest_file: "SUSEMono-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
