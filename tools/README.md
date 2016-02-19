# Tools

## Sample Usage

Compare fonts:

    python compare_font.py font1.ttf font2.ttf;

Add a METADATA.pb to a family directory

    python add_font.py ../ofl/newfamily;

Sanity check a family directory:

    python sanity_check.py --repair_script=/tmp/fix.py ../ofl/josefinsans;
    python sanity_check.py --repair_script=/tmp/fix.py --fix_type=fsSelection ../ufl;

## Dependencies

To use `compare_font.py` and `sanity_check.py` you will need:

* https://github.com/google/google-apputils
* https://github.com/google/protobuf
* https://github.com/behdad/fonttools

These can be installed with pip:

    sudo easy_install pip;
    sudo pip install google-apputils protobuf git+git://github.com/behdad/fonttools.git;

## License

The tools and files under this directory are available under the Apache License v2.0, for details see [LICENSE.txt](LICENSE.txt)
