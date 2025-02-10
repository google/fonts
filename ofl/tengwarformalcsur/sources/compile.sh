#!/bin/bash

fontforge -script dansmith2unicode.py

cp TengwarFormalCSUR_dumb.ttf TengwarFormalCSUR_AAT.ttf
ftxenhancer -m TengwarFormalCSUR.mif TengwarFormalCSUR_AAT.ttf

grcompiler TengwarFormalCSUR.gdl TengwarFormalCSUR_AAT.ttf TengwarFormalCSUR.ttf
