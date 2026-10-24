name: "PT Sans Caption"
designer: "ParaType"
license: "OFL"
category: "SANS_SERIF"
date_added: "2010-09-21"
fonts {
  name: "PT Sans Caption"
  style: "normal"
  weight: 400
  filename: "PT_Sans-Caption-Web-Regular.ttf"
  post_script_name: "PTSans-Caption"
  full_name: "PT Sans Caption"
  copyright: "Copyright © 2009 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
fonts {
  name: "PT Sans Caption"
  style: "normal"
  weight: 700
  filename: "PT_Sans-Caption-Web-Bold.ttf"
  post_script_name: "PTSans-CaptionBold"
  full_name: "PT Sans Caption Bold"
  copyright: "Copyright © 2009 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
subsets: "menu"
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
source {
  repository_url: "https://github.com/googlefonts/ptsanscaption"
  commit: "6c1efcf8b0d2f413ad47ff12512ee7e0b9e54b75"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/PTSansCaption-Bold.ttf"
    dest_file: "PT_Sans-Caption-Web-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/PTSansCaption-Regular.ttf"
    dest_file: "PT_Sans-Caption-Web-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
