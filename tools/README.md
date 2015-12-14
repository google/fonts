# Tools

# License

The tools under this directory are available under the Apache License v2.0.
See [LICENSE.txt](LICENSE.txt) for details.

# Sample Usage

compare_font
```
python compare_font.py font1.ttf font2.ttf
```

sanity_check
```
python sanity_check.py --repair_script=/tmp/fix.py ../ofl/josefinsans
python sanity_check.py --repair_script=/tmp/fix.py --fix_type=fsSelection ../ufl
```

## Dependencies

To use compare_font and sanity_check you will need:

* https://github.com/google/google-apputils.
* https://github.com/behdad/fonttools.

To use sanity_check you will additionally need:

* https://github.com/google/protobuf
