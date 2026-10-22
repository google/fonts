name: "PT Sans Narrow"
designer: "ParaType"
license: "OFL"
category: "SANS_SERIF"
date_added: "2010-09-21"
fonts {
  name: "PT Sans Narrow"
  style: "normal"
  weight: 400
  filename: "PT_Sans-Narrow-Web-Regular.ttf"
  post_script_name: "PTSans-Narrow"
  full_name: "PT Sans Narrow"
  copyright: "Copyright © 2009 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
fonts {
  name: "PT Sans Narrow"
  style: "normal"
  weight: 700
  filename: "PT_Sans-Narrow-Web-Bold.ttf"
  post_script_name: "PTSans-NarrowBold"
  full_name: "PT Sans Narrow Bold"
  copyright: "Copyright © 2009 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
subsets: "menu"
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
source {
  repository_url: "https://github.com/googlefonts/ptsansnarrow"
  commit: "ff02de9bb277e04d35751bac43e7df176f1382c8"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/PTSansNarrow-Bold.ttf"
    dest_file: "PT_Sans-Narrow-Web-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/PTSansNarrow-Regular.ttf"
    dest_file: "PT_Sans-Narrow-Web-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
