name: "Nabla"
designer: "Arthur Reinders Folmer, Just van Rossum"
license: "OFL"
category: "DISPLAY"
date_added: "2022-08-15"
fonts {
  name: "Nabla"
  style: "normal"
  weight: 400
  filename: "Nabla[EDPT,EHLT].ttf"
  post_script_name: "Nabla-Regular"
  full_name: "Nabla Regular"
  copyright: "Copyright 2022 The Nabla Project Authors (https://github.com/justvanrossum/nabla)"
}
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "EDPT"
  min_value: 0.0
  max_value: 200.0
}
axes {
  tag: "EHLT"
  min_value: 0.0
  max_value: 24.0
}
source {
  repository_url: "https://github.com/justvanrossum/nabla"
  archive_url: "https://github.com/justvanrossum/nabla/releases/download/v1.002/nabla-fonts.zip"
  files {
    source_file: "nabla-fonts/Nabla[EDPT,EHLT].ttf"
    dest_file: "Nabla[EDPT,EHLT].ttf"
  }
  branch: "main"
}
minisite_url: "https://nabla.typearture.com/"
