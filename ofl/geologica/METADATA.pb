name: "Geologica"
designer: "Monokrom, Sindre Bremnes, Frode Helland"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-04-12"
fonts {
  name: "Geologica"
  style: "normal"
  weight: 400
  filename: "Geologica[CRSV,SHRP,slnt,wght].ttf"
  post_script_name: "Geologica-Thin"
  full_name: "Geologica Thin"
  copyright: "Copyright 2020 The Geologica Project Authors (https://github.com/googlefonts/geologica)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "greek"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "CRSV"
  min_value: 0.0
  max_value: 1.0
}
axes {
  tag: "SHRP"
  min_value: 0.0
  max_value: 100.0
}
axes {
  tag: "slnt"
  min_value: -12.0
  max_value: 0.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
registry_default_overrides {
  key: "CRSV"
  value: 0.0
}
source {
  repository_url: "https://github.com/googlefonts/geologica"
  commit: "685f38d7c9e86b0c8530204c97ddcaf6558dd17b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/Geologica[CRSV,SHRP,slnt,wght].ttf"
    dest_file: "Geologica[CRSV,SHRP,slnt,wght].ttf"
  }
  branch: "main"
}
