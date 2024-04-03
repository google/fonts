name: "Monda"
designer: "Vernon Adams"
license: "OFL"
category: "SANS_SERIF"
date_added: "2012-11-30"
fonts {
  name: "Monda"
  style: "normal"
  weight: 400
  filename: "Monda-Regular.ttf"
  post_script_name: "Monda-Regular"
  full_name: "Monda Regular"
  copyright: "Copyright 2021 The Monda Project Authors (https://github.com/googlefonts/mondaFont)"
}
fonts {
  name: "Monda"
  style: "normal"
  weight: 700
  filename: "Monda-Bold.ttf"
  post_script_name: "Monda-Bold"
  full_name: "Monda Bold"
  copyright: "Copyright 2021 The Monda Project Authors (https://github.com/googlefonts/mondaFont)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
source {
  repository_url: "https://github.com/googlefonts/mondaFont"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Monda-Bold.ttf"
    dest_file: "Monda-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Monda-Regular.ttf"
    dest_file: "Monda-Regular.ttf"
  }
  branch: "master"
}
