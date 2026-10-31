name: "PT Sans"
designer: "ParaType"
license: "OFL"
category: "SANS_SERIF"
date_added: "2010-09-21"
fonts {
  name: "PT Sans"
  style: "normal"
  weight: 400
  filename: "PT_Sans-Web-Regular.ttf"
  post_script_name: "PTSans-Regular"
  full_name: "PT Sans"
  copyright: "Copyright © 2009 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
fonts {
  name: "PT Sans"
  style: "italic"
  weight: 400
  filename: "PT_Sans-Web-Italic.ttf"
  post_script_name: "PTSans-Italic"
  full_name: "PT Sans Italic"
  copyright: "Copyright © 2009 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
fonts {
  name: "PT Sans"
  style: "normal"
  weight: 700
  filename: "PT_Sans-Web-Bold.ttf"
  post_script_name: "PTSans-Bold"
  full_name: "PT Sans Bold"
  copyright: "Copyright © 2009 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
fonts {
  name: "PT Sans"
  style: "italic"
  weight: 700
  filename: "PT_Sans-Web-BoldItalic.ttf"
  post_script_name: "PTSans-BoldItalic"
  full_name: "PT Sans Bold Italic"
  copyright: "Copyright © 2009 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
subsets: "menu"
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
source {
  repository_url: "https://github.com/googlefonts/ptsans"
  commit: "bcb93f7b9b2c39cf3c75d87be570444f91d0f0b6"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/PTSans-Bold.ttf"
    dest_file: "PT_Sans-Web-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/PTSans-BoldItalic.ttf"
    dest_file: "PT_Sans-Web-BoldItalic.ttf"
  }
  files {
    source_file: "fonts/ttf/PTSans-Italic.ttf"
    dest_file: "PT_Sans-Web-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/PTSans-Regular.ttf"
    dest_file: "PT_Sans-Web-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
