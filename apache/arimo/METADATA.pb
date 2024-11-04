name: "Arimo"
designer: "Steve Matteson"
license: "APACHE2"
category: "SANS_SERIF"
date_added: "2010-11-18"
fonts {
  name: "Arimo"
  style: "normal"
  weight: 400
  filename: "Arimo[wght].ttf"
  post_script_name: "Arimo-Regular"
  full_name: "Arimo Regular"
  copyright: "Copyright 2020 The Arimo Project Authors (https://github.com/googlefonts/arimo)"
}
fonts {
  name: "Arimo"
  style: "italic"
  weight: 400
  filename: "Arimo-Italic[wght].ttf"
  post_script_name: "Arimo-Italic"
  full_name: "Arimo Italic"
  copyright: "Copyright 2020 The Arimo Project Authors (https://github.com/googlefonts/arimo)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "greek"
subsets: "greek-ext"
subsets: "hebrew"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/TypeNetwork/Arimo"
  files {
    source_file: "LICENSE.txt"
    dest_file: "LICENSE.txt"
  }
  files {
    source_file: "fonts/ttf/Arimo-Bold.ttf"
    dest_file: "static/Arimo-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Arimo-BoldItalic.ttf"
    dest_file: "static/Arimo-BoldItalic.ttf"
  }
  files {
    source_file: "fonts/ttf/Arimo-Italic.ttf"
    dest_file: "static/Arimo-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/Arimo-Regular.ttf"
    dest_file: "static/Arimo-Regular.ttf"
  }
  files {
    source_file: "fonts/vf/Arimo-Italic[wght].ttf"
    dest_file: "Arimo-Italic[wght].ttf"
  }
  files {
    source_file: "fonts/vf/Arimo[wght].ttf"
    dest_file: "Arimo[wght].ttf"
  }
  branch: "master"
}
