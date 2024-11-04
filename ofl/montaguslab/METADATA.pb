name: "Montagu Slab"
designer: "Florian Karsten"
license: "OFL"
category: "SERIF"
date_added: "2021-09-21"
fonts {
  name: "Montagu Slab"
  style: "normal"
  weight: 400
  filename: "MontaguSlab[opsz,wght].ttf"
  post_script_name: "MontaguSlab-Bold"
  full_name: "Montagu Slab Bold"
  copyright: "Copyright 2021 The Montagu Slab Project Authors (https://github.com/floriankarsten/montagu-slab)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "opsz"
  min_value: 16.0
  max_value: 144.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 700.0
}
registry_default_overrides {
  key: "opsz"
  value: 144.0
}
source {
  repository_url: "https://github.com/floriankarsten/montagu-slab"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/MontaguSlab[opsz,wght].ttf"
    dest_file: "MontaguSlab[opsz,wght].ttf"
  }
  branch: "master"
}
stroke: "SLAB_SERIF"
classifications: "DISPLAY"
