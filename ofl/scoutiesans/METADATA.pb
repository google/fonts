name: "Scoutie Sans"
designer: "Tyler Finck"
license: "OFL"
category: "SANS_SERIF"
date_added: "2026-05-20"
fonts {
  name: "Scoutie Sans"
  style: "normal"
  weight: 400
  filename: "ScoutieSans[wght].ttf"
  post_script_name: "ScoutieSans-Regular"
  full_name: "Scoutie Sans Regular"
  copyright: "Copyright 2026 The Scoutie Sans Project Authors (https://www.helpscout.com)"
}
fonts {
  name: "Scoutie Sans"
  style: "italic"
  weight: 400
  filename: "ScoutieSans-Italic[wght].ttf"
  post_script_name: "ScoutieSans-Italic"
  full_name: "Scoutie Sans Italic"
  copyright: "Copyright 2026 The Scoutie Sans Project Authors (https://www.helpscout.com)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 200
  max_value: 800
}
source {
  repository_url: "https://github.com/sursly/scoutie"
  branch: "main"
  files {
    source_file: "sources/Scoutie-Sans.glyphs"
    dest_file: "ScoutieSans[wght].ttf"
  }
  files {
    source_file: "sources/Scoutie-Sans-Italic.glyphs"
    dest_file: "ScoutieSans-Italic[wght].ttf"
  }
  type: "UPSTREAM_REPO"
}
is_noto: false
