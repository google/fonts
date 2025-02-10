#!/usr/local/bin/fontforge

import fontforge
import psMat

outfont=fontforge.font()
outfont.encoding="unicode"
outfont.em=2048
for layer in outfont.layers:
  outfont.layers[layer].is_quadratic = True;

outfont.fontname='TengwarFormalCSUR-Regular'
outfont.familyname='Tengwar Formal CSUR'
outfont.fullname='Tengwar Formal CSUR'
outfont.copyright='Copyright (c) September 2009, Michal Nowakowski (http://tengwarformal.limes.com.pl),\n\
with Reserved Font Names "Tengwar Formal" and "Tengwar Formal A".\n\
\n\
Tengwar Formal CSUR copyright (c) 2010-2012, Johan Winge and J. "Mach" Wust (http://freetengwar.sourceforge.net/)\n\
\n\
This Font Software is licensed under the SIL Open Font License, Version 1.1.\n\
This license is provided in a separate file, LICENSE.txt, supplied with the fonts,\n\
and is also available with a FAQ at: http://scripts.sil.org/OFL'
outfont.version='1.1'
outfont.sfnt_names=(('English (US)', 'UniqueID', 'FontTengwarFormalCSUR11'),
                    ('English (US)', 'Designer', 'Micha\xc5\x82 Nowakowski'),
                    ('English (US)', 'Designer URL', 'http://tengwarformal.limes.com.pl'),
                    ('English (US)', 'License URL', 'http://scripts.sil.org/OFL'),
                    ('English (US)', 'Vendor URL', 'http://freetengwar.sourceforge.net/')
                   )

## List the source font files, their glyphs, and what these glyphs should be mapped to.
dansmithenc ={fontforge.open("TengwarFormal12c.sfd"): {
               'one': 'tinco',
               'q': 'parma',
               'a': 'calma',
               'z': 'quesse',
               'two': 'ando',
               'w': 'umbar',
               's': 'anga',
               'x': 'ungwe',
               'three': 'suule',
               'e': 'formen',
               'd': 'aha',
               'c': 'hwesta',
               'four': 'anto',
               'r': 'ampa',
               'f': 'anca',
               'v': 'unque',
               'five': 'nuumen',
               't': 'malta',
               'g': 'noldo',
               'b': 'nwalme',
               'six': 'oore',
               'y': 'vala',
               'h': 'anna',
               'n': 'vilya',
               'exclam': 'tincoX',
               'Q': 'parmaX',
               'A': 'calmaX',
               'Z': 'quesseX',
               'at': 'andoX',
               'W': 'umbarX',
               'S': 'angaX',
               'X': 'ungweX',
               'seven': 'roomen',
               'u': 'arda',
               'j': 'lambe',
               'm': 'alda',
               'eight': 'silme',
               'i': 'silmeN',
               'k': 'esse',
               'comma': 'esseN',
               'asterisk': 'silme.alt',
               'I': 'silmeN.alt',
               'K': 'esse.alt',
               'less': 'esseN.alt', # Or hwestaC
               'nine': 'hyarmen',
               'o': 'hwestaS',
               'l': 'yanta',
               'period': 'uure',
               'asciitilde': 'longCarrier',
               'onehalf': 'halla',
               'grave': 'shortCarrier',
               'threequarters': 'lambeN',
               'threesuperior': 'lambeN.alt',
               'bracketright': 'osse',
               'daggerdbl': 'osse.alt',
               'onequarter': 'carrierX',
               #'Adieresis': 'quesseC', # Use a newly drawn glyph instead
               'questiondown': 'roomenN',
               'scaron': 'maltaX',
               'bullet': 'hallaRoomen.alt',
               'numbersign': 'tehtaA.shift4',
               'E': 'tehtaA.shift3',
               'D': 'tehtaA.shift2',
               'C': 'tehtaA.shift1',
               'Udieresis': 'tehtaA.altshift4',
               'Yacute': 'tehtaA.altshift3',
               'Thorn': 'tehtaA.altshift2',
               'germandbls': 'tehtaA.altshift1',
               'Eth': 'tehtaAB.shift4',
               'Ntilde': 'tehtaAB.shift3',
               'Ograve': 'tehtaAB.shift2',
               'Oacute': 'tehtaAB.shift1',
               #'greater': 'tehtaAB.shift1alt', # Might be duplicate
               'Ocircumflex': 'tehtaY.shift4',
               'Otilde': 'tehtaY.shift3',
               'Odieresis': 'tehtaY.shift2',
               'multiply': 'tehtaY.shift1',
               'Igrave': 'tehtaYB.shift4',
               'Iacute': 'tehtaYB.shift3',
               'Icircumflex': 'tehtaYB.shift2',
               'Idieresis': 'tehtaYB.shift1',
               'acute': 'tehtaYB.lambeoriginal',
               'percent': 'tehtaI.shift4',
               'T': 'tehtaI.shift3',
               'G': 'tehtaI.shift2',
               'B': 'tehtaI.shift1',
               'parenleft': 'tehtaIB.shift4',
               #'Egrave': 'tehtaIB.shift4alt', # Might be duplicate
               'Eacute': 'tehtaIB.shift35',   # Might be duplicate
               'O': 'tehtaIB.shift3',
               'Ecircumflex': 'tehtaIB.shift2',
               'Edieresis': 'tehtaIB.shift1',
               'L': 'tehtaIB.lambeoriginal',
               'dollar': 'tehtaE.shift4',
               'R': 'tehtaE.shift3',
               'F': 'tehtaE.shift2',
               'V': 'tehtaE.shift1',
               'perthousand': 'tehtaEB.shift4',
               'Scaron': 'tehtaEB.shift3',
               'guilsinglleft': 'tehtaEB.shift2',
               'Ydieresis': 'tehtaEB.shift1',
               'florin': 'tehtaEEB.shift4',
               'quotedblbase': 'tehtaEEB.shift3',
               'ellipsis': 'tehtaEEB.shift2',
               'dagger': 'tehtaEEB.shift1',
               'quotesinglbase': 'tehtaEEB.lambe',
               'asciicircum': 'tehtaO.shift4',
               'Y': 'tehtaO.shift3',
               'H': 'tehtaO.shift2',
               'N': 'tehtaO.shift1',
               'adieresis': 'tehtaOB.shift4',
               'aring': 'tehtaOB.shift3',
               'ae': 'tehtaOB.shift2',
               'ccedilla': 'tehtaOB.shift1',
               'ampersand': 'tehtaU.shift4',
               'U': 'tehtaU.shift3',
               'J': 'tehtaU.shift2',
               'M': 'tehtaU.shift1',
               'agrave': 'tehtaU.altshift4',
               'aacute': 'tehtaU.altshift3',
               'acircumflex': 'tehtaU.altshift2',
               'atilde': 'tehtaU.altshift1',
               'quoteleft': 'tehtaUB.shift4',
               'quoteright': 'tehtaUB.shift3',
               'quotedblleft': 'tehtaUB.shift2',
               'quotedblright': 'tehtaUB.shift1',
               'bracketleft': 'tehtaN.narrow',
               'braceleft': 'tehtaN.wide',
               'icircumflex': 'tehtaN.highnarrow',
               'igrave': 'tehtaN.highwide',
               'p': 'tehtaN.altnarrow',
               'P': 'tehtaN.altwide',
               'zero': 'tehtaN.althighnarrow',
               'parenright': 'tehtaN.althighwide',
               'quotesingle': 'tehtaB.narrow',
               'quotedbl': 'tehtaB.wide',
               'cedilla': 'tehtaB.lambe',
               'idieresis': 'tehtaB.lownarrow',
               'iacute': 'tehtaB.lowwide',
               'semicolon': 'tehtaB.altnarrow',
               'colon': 'tehtaB.altwide',
               'slash': 'tehtaB.altlownarrow',
               'degree': 'tehtaB.altlambe',
               'question': 'tehtaB.altlowwide',
               'egrave': 'tehtaW.giantshift4',
               'eacute': 'tehtaW.giantshift3',
               'ecircumflex': 'tehtaW.giantshift2',
               'edieresis': 'tehtaW.giantshift1',
               'ordfeminine': 'tehtaAE.shift4',
               'minus': 'tehtaAE.shift3',
               #'Euro': 'tehtaAE.shift3alt', # Might be duplicate
               'macron': 'tehtaAE.shift2',
               'mu1': 'tehtaAE.shift1',
               'Oslash': 'tehtaAE.altshift4', # Note that people use this as the breve...
               'Ugrave': 'tehtaAE.altshift3',
               'Uacute': 'tehtaAE.altshift2',
               'Ucircumflex': 'tehtaAE.altshift1',
               'udieresis': 'tehtaThinnas.shift4',
               'yacute': 'tehtaThinnas.shift3',
               'thorn': 'tehtaThinnas.shift2',
               'ydieresis': 'tehtaThinnas.shift1',
               'plus': 'tehtaS',
               'underscore': 'tehtaX.down',
               'sterling': 'tehtaS.swash',
               'yen': 'tehtaS.swashlambe',
               'Aring': 'tehtaS.upward',
               'cent': 'tehtaS.raised',
               'AE': 'tehtaS.raisedupward',
               'exclamdown': 'tehtaS.lifted',
               'bar': 'tehtaX.shift4',
               'braceright': 'tehtaX.shift3',
               'equal': 'tengwarPusta',
               'hyphen': 'tengwarDoublepusta',
               'circumflex': 'tengwarTriplepusta',
               'Aacute': 'tengwarExclamation',
               'Agrave': 'tengwarQuestion',
               'guilsinglright': 'tengwarParenthesis',
               'backslash': 'tengwarSection',
               'Acircumflex': 'tengwarSection.wide',
               'logicalnot': 'tengwarDoublesection',
               'guillemotleft': 'tengwarQuoteleft',
               'guillemotright': 'tengwarQuoteright',
               'eth': 'tengwardigit0',
               'ntilde': 'tengwardigit1',
               'ograve': 'tengwardigit2',
               'oacute': 'tengwardigit3',
               'ocircumflex': 'tengwardigit4',
               'otilde': 'tengwardigit5',
               'odieresis': 'tengwardigit6',
               'divide': 'tengwardigit7',
               'oslash': 'tengwardigit8',
               'ugrave': 'tengwardigit9',
               'uacute': 'tengwarduodecimal10',
               'ucircumflex': 'tengwarduodecimal11',
               'tilde': 'tengwardigitMark.shift4',
               'trademark': 'tengwardigitMark.shift3',
               'dieresis': 'tengwardigitMark.shift2',
               'copyright': 'tengwardigitMark.shift1',
               'section': 'aha_tinco',
               'brokenbar': 'hwesta_tinco',
               'endash': 'silme_aha',
               'emdash': 'uni204A',
               'plusminus': 'quoteleft',
               'twosuperior': 'quoteright',
               'registered': 'question',
               'Ccedilla': 'exclam',
               'ordmasculine': 'period',
               'Atilde': 'semicolon',
               'onesuperior': 'comma',
               'OE': 'parenleft',
               'oe': 'parenright',
               'space': 'space',
               'paragraph': 'paragraph',
               'middot': 'middot',
               'currency': 'currency',
              },

              fontforge.open("TengwarFormalA12c.sfd"): {
               'seven': 'roomen.alt',
               'u': 'arda.alt',
               'less': 'hwestaC',
               'y': 'valaX',
               'questiondown': 'roomenN.alt',
               'percent': 'tehtaYanta.shift4',
               'T': 'tehtaYanta.shift3',
               'G': 'tehtaYanta.shift2',
               'B': 'tehtaYanta.shift1',
               'numbersign': 'tehtaUure.shift4', # Not encoded in the unicode font
               'E': 'tehtaUure.shift3',
               'D': 'tehtaUure.shift2',
               'C': 'tehtaUure.shift1',
               'asciicircum': 'tehtaBreve.shift4',
               'Y': 'tehtaBreve.shift3',
               'H': 'tehtaBreve.shift2',
               'N': 'tehtaBreve.shift1',
               'dollar': 'tehtaW.shift4',
               'R': 'tehtaW.shift3',
               'F': 'tehtaW.shift2',
               'V': 'tehtaW.shift1',
               'braceright': 'tehtaS.swashhyarmen',
              },

              fontforge.open("TengwarFormalCSUR-addchar.sfd"): {
               'tengwarQuadruplepusta': 'tengwarQuadruplepusta',
               'uni10FB': 'uni10FB',
               'uni2E2C': 'uni2E2C',
               'tengwarQuintuplepusta': 'tengwarQuintuplepusta',
               'annaX': 'annaX',
               'quesseC': 'quesseC',
               'hallaRoomen': 'hallaRoomen',
               'vaiya': 'vaiya',
               'tengwarduodecimal12': 'tengwarduodecimal12',
               'tehtaGrave.shift1': 'tehtaGrave.shift1',
               'tehtaGrave.shift2': 'tehtaGrave.shift2',
               'tehtaGrave.shift3': 'tehtaGrave.shift3',
               'tehtaGrave.shift4': 'tehtaGrave.shift4',
               'tehtaDotInside': 'tehtaDotInside',
               'tehtaN.narrowlow': 'tehtaN.narrowlow',
               'tehtaN.widelow': 'tehtaN.widelow',
               'tehtaN.altnarrowlow': 'tehtaN.altnarrowlow',
               'tehtaN.altwidelow': 'tehtaN.altwidelow',
               'tehtaN.shift1': 'tehtaN.shift1',
               'tehtaN.shift1low': 'tehtaN.shift1low',
               'tehtaN.altshift1': 'tehtaN.altshift1',
               'tehtaN.altshift1low': 'tehtaN.altshift1low',
               'tehtaB.shift1': 'tehtaB.shift1',
               'tehtaB.altshift1': 'tehtaB.altshift1',
               'tehtaW.combshift1': 'tehtaW.combshift1',
               'tehtaW.combshift2': 'tehtaW.combshift2',
               'tehtaW.combshift3': 'tehtaW.combshift3',
               'tehtaW.combshift4': 'tehtaW.combshift4',
               'tehtaE_tehtaE.shift1': 'tehtaE_tehtaE.shift1',
               'tehtaE_tehtaE.shift2': 'tehtaE_tehtaE.shift2',
               'tehtaE_tehtaE.shift3': 'tehtaE_tehtaE.shift3',
               'tehtaE_tehtaE.shift4': 'tehtaE_tehtaE.shift4',
               'tehtaO_tehtaI.shift1': 'tehtaO_tehtaI.shift1',
               'tehtaO_tehtaI.shift2': 'tehtaO_tehtaI.shift2',
               'tehtaO_tehtaI.shift3': 'tehtaO_tehtaI.shift3',
               'tehtaO_tehtaI.shift4': 'tehtaO_tehtaI.shift4',
               'tehtaO_tehtaO.shift1': 'tehtaO_tehtaO.shift1',
               'tehtaO_tehtaO.shift2': 'tehtaO_tehtaO.shift2',
               'tehtaO_tehtaO.shift3': 'tehtaO_tehtaO.shift3',
               'tehtaO_tehtaO.shift4': 'tehtaO_tehtaO.shift4',
               'tehtaU_tehtaI.shift1': 'tehtaU_tehtaI.shift1',
               'tehtaU_tehtaI.shift2': 'tehtaU_tehtaI.shift2',
               'tehtaU_tehtaI.shift3': 'tehtaU_tehtaI.shift3',
               'tehtaU_tehtaI.shift4': 'tehtaU_tehtaI.shift4',
               'tehtaU_tehtaU.shift1': 'tehtaU_tehtaU.shift1',
               'tehtaU_tehtaU.shift2': 'tehtaU_tehtaU.shift2',
               'tehtaU_tehtaU.shift3': 'tehtaU_tehtaU.shift3',
               'tehtaU_tehtaU.shift4': 'tehtaU_tehtaU.shift4',
               'tehtaS.raisedalt': 'tehtaS.raisedalt',
               'tehtaS.raisedlambe': 'tehtaS.raisedlambe',
               'tehtaS.aha': 'tehtaS.aha',
               'tehtaS.lambelow': 'tehtaS.lambelow',
               'tehtaS.hyarmen': 'tehtaS.hyarmen',
               'tehtaS.yanta': 'tehtaS.yanta',
               'tehtaS.swashraised': 'tehtaS.swashraised',
               'tehtaS.swashraisedlambe': 'tehtaS.swashraisedlambe',
               'tehtaS.swashyanta': 'tehtaS.swashyanta',
               'tehtaS.swashyantaalt': 'tehtaS.swashyantaalt',
               'tehtaS.swashhyarmenalt': 'tehtaS.swashhyarmenalt',
               'tehtaGrave_tehtaGrave.shift1': 'tehtaGrave_tehtaGrave.shift1',
               'tehtaGrave_tehtaGrave.shift2': 'tehtaGrave_tehtaGrave.shift2',
               'tehtaGrave_tehtaGrave.shift3': 'tehtaGrave_tehtaGrave.shift3',
               'tehtaGrave_tehtaGrave.shift4': 'tehtaGrave_tehtaGrave.shift4',
               'tehtaYB.lambe': 'tehtaYB.lambe',
               'tehtaIB.lambe': 'tehtaIB.lambe',
               'tengwarExclamationB': 'tengwarExclamationB',
              }}

## Apart from all the glyphs above, we also define some new ones by referencing other glyphs:
## Format: (new glyph, original glyph, transformation, width)
## The function that deals with this list later on sets a width < 0 to the width of the original glyph.
references = [('tehtaA','tehtaA.shift2',psMat.identity(),0),
              ('tehtaAB','tehtaAB.shift2',psMat.identity(),0),
              ('tehtaY','tehtaY.shift2',psMat.identity(),0),
              ('tehtaYB','tehtaYB.shift2',psMat.identity(),0),
              ('tehtaI','tehtaI.shift2',psMat.identity(),0),
              ('tehtaIB','tehtaIB.shift2',psMat.identity(),0),
              ('tehtaE','tehtaE.shift2',psMat.identity(),0),
              ('tehtaEB','tehtaEB.shift2',psMat.identity(),0),
              ('tehtaEEB','tehtaEEB.shift2',psMat.identity(),0),
              ('tehtaO','tehtaO.shift2',psMat.identity(),0),
              ('tehtaOB','tehtaOB.shift2',psMat.identity(),0),
              ('tehtaU','tehtaU.shift2',psMat.identity(),0),
              ('tehtaUB','tehtaUB.shift2',psMat.identity(),0),
              ('tehtaN','tehtaN.narrow',psMat.identity(),0),
              ('tehtaB','tehtaB.narrow',psMat.identity(),0),
              ('tehtaW','tehtaW.shift2',psMat.identity(),0),
              ('tehtaBreve','tehtaBreve.shift2',psMat.identity(),0),
              ('tehtaGrave','tehtaGrave.shift2',psMat.identity(),0),
              ('tehtaYanta','tehtaYanta.shift2',psMat.identity(),0),
              ('tehtaAE','tehtaAE.shift2',psMat.identity(),0),
              ('tehtaThinnas','tehtaThinnas.shift2',psMat.identity(),0),
              ('tehtaX','tehtaX.shift3',psMat.identity(),0),
              ('uni2E31','tengwarPusta',psMat.identity(),-1),
              ('colon','tengwarDoublepusta',psMat.identity(),-1),
              ('uni205D','tengwarTriplepusta',psMat.identity(),-1),
              ('uni2058','tengwarQuadruplepusta',psMat.identity(),-1),
              ('uni2E2D','tengwarQuintuplepusta',psMat.identity(),-1),
              ('osseN','tengwardigit0',psMat.identity(),-1),
              ('tengwardigitMark','tengwardigitMark.shift2',psMat.identity(),-1),
             ]

## The Free Tengwar Font Project encoding. Mapping of the new glyph names to their Unicode position:
freetengenc = {'tinco': 0xE000,
               'parma': 0xE001,
               'calma': 0xE002,
               'quesse': 0xE003,
               'ando': 0xE004,
               'umbar': 0xE005,
               'anga': 0xE006,
               'ungwe': 0xE007,
               'suule': 0xE008,
               'formen': 0xE009,
               'aha': 0xE00A,
               'hwesta': 0xE00B,
               'anto': 0xE00C,
               'ampa': 0xE00D,
               'anca': 0xE00E,
               'unque': 0xE00F,
               'nuumen': 0xE010,
               'malta': 0xE011,
               'noldo': 0xE012,
               'nwalme': 0xE013,
               'oore': 0xE014,
               'vala': 0xE015,
               'anna': 0xE016,
               'vilya': 0xE017,
               'tincoX': 0xE018,
               'parmaX': 0xE019,
               'calmaX': 0xE01A,
               'quesseX': 0xE01B,
               'andoX': 0xE01C,
               'umbarX': 0xE01D,
               'angaX': 0xE01E,
               'ungweX': 0xE01F,
               'roomen': 0xE020,
               'arda': 0xE021,
               'lambe': 0xE022,
               'alda': 0xE023,
               'silme': 0xE024,
               'silmeN': 0xE025,
               'esse': 0xE026,
               'esseN': 0xE027,
               'hyarmen': 0xE028,
               'hwestaS': 0xE029,
               'yanta': 0xE02A,
               'uure': 0xE02B,
               'longCarrier': 0xE02C,
               'halla': 0xE02D,
               'shortCarrier': 0xE02E,
               'osseN': 0xE030,
               'lambeN': 0xE031,
               'osse': 0xE032,
               'carrierX': 0xE034,
               'annaS': 0xE035,
               'annaX': 0xE036,
               'quesseC': 0xE037,
               'hwestaC': 0xE038,
               'roomenN': 0xE039,
               'maltaX': 0xE03A,
               'valaX': 0xE03B,
               'hallaRoomen': 0xE03C,
               'vaiya': 0xE03D,
               'tehtaA': 0xE040,
               'tehtaAB': 0xE041,
               'tehtaY': 0xE042,
               'tehtaYB': 0xE043,
               'tehtaI': 0xE044,
               'tehtaIB': 0xE045,
               'tehtaE': 0xE046,
               'tehtaEB': 0xE047,
               'tehtaEE': 0xE048,
               'tehtaEEB': 0xE049,
               'tehtaO': 0xE04A,
               'tehtaOB': 0xE04B,
               'tehtaU': 0xE04C,
               'tehtaUB': 0xE04D,
               'tehtaOO': 0xE04E,
               'tehtaUU': 0xE04F,
               'tehtaN': 0xE050,
               'tehtaB': 0xE051,
               'tehtaW': 0xE052,
               'tehtaBreve': 0xE053,
               'tehtaGrave': 0xE054,
               'tehtaYanta': 0xE055,
               'tehtaAE': 0xE056,
               'tehtaThinnas': 0xE057,
               'tehtaS': 0xE058,
               'tehtaX': 0xE059,
               'tehtaDotInside': 0xE05A,
               'tengwarPusta': 0xE060,
               'tengwarDoublepusta': 0xE061,
               'tengwarTriplepusta': 0xE062,
               'tengwarQuadruplepusta': 0xE063,
               'tengwarQuintuplepusta': 0xE064,
               'tengwarExclamation': 0xE065,
               'tengwarQuestion': 0xE066,
               'tengwarParenthesis': 0xE067,
               'tengwarSection': 0xE068,
               'tengwarDoublesection': 0xE069,
               'tengwarQuoteleft': 0xE06A,
               'tengwarQuoteright': 0xE06B,
               'tengwarExclamationB': 0xE06C,
               'tengwardigit0': 0xE070,
               'tengwardigit1': 0xE071,
               'tengwardigit2': 0xE072,
               'tengwardigit3': 0xE073,
               'tengwardigit4': 0xE074,
               'tengwardigit5': 0xE075,
               'tengwardigit6': 0xE076,
               'tengwardigit7': 0xE077,
               'tengwardigit8': 0xE078,
               'tengwardigit9': 0xE079,
               'tengwarduodecimal10': 0xE07A,
               'tengwarduodecimal11': 0xE07B,
               'tengwarduodecimal12': 0xE07C,
               'tengwardigitMark': 0xE07D,
              }

## You can choose if the glyphs in the final font should have names which
## describe them ("tehtaA.shift3"), or names which map to the Unicode position ("uniE040.shift3").
## This makes a difference in one very specific circumstance:
## when copying text from a PDF file, a variant glyph named, e.g., "uniE040.shift3"
## will be copied as U+E040, but "tehtaA.shift3" will not be copied as a Unicode character.
## However, the MIF file currently depends on the glyph names being descriptive:
descriptiveglyphnames=True

## A function to replace glyphnames with the unicode value. For example:
##   tinco  ->  uniE000
##   hwesta_tinco.var1  ->  uniE00B_uniE000.var1
## If descriptiveglyphnames is set to True, this function is only used
## to give a means to sort the glyphs in a sensible order.
def ucname(alias):
   if '.' in alias:
     (base,var)=alias.split('.',1)
     var='.'+var
   else:
     (base,var)=(alias,'')
   name=''
   for comp in base.split('_'):
     if len(name)>0:
       name=name+'_'
     if comp in freetengenc:
       name=name+'uni' + hex(freetengenc[comp])[2:].upper()
     else:
       name=name+comp
   return name+var

gdh=open('TengwarFormalCSUR.gdh','w')
gdh.write('table(glyph)\n')

## Copy all the glyphs from the original fonts, according to the mapping defined above.
## References can not simply be copied, so they are added to the list of references,
## which in turn is handled later.
for thefont, encoding in dansmithenc.iteritems():
   for char, alias in sorted(encoding.iteritems(), lambda x, y: cmp(ucname(x[1]),ucname(y[1]))):
      if descriptiveglyphnames:
         ucchar=alias
      else:
         ucchar=ucname(alias)
      thefont.selection.select(char)
      for ref in thefont[char].references:
         if thefont[ref[0]].unicode>0 and ref[0] in encoding:
            newrefname=encoding[ref[0]]
         else:
            newrefname=ref[0]
         references.append((ucchar,newrefname,ref[1],thefont[char].width))
      thefont[char].references=()
      thefont.copy()
      thefont.clear()
      outfont.createChar(fontforge.unicodeFromName(ucchar),ucchar).width=thefont[char].width
      outfont.selection.select(ucchar)
      outfont.paste()
      if ucchar in outfont:
        outfont[ucchar].references=()
        gdh.write('  ' + alias.replace('.', '_') + ' = ps("' + ucchar + '");\n')
      if alias in freetengenc:
        outfont[ucchar].unicode=freetengenc[alias]

outfont.createChar(0x200B,"zwsp").width=0
outfont.createChar(0x200C,"zwnj").width=0
outfont.createChar(0x200D,"zwj").width=0
gdh.write('  ZWJ = ps("zwj");\n')

## Create referenced glyphs.
for (aliastarget, ref, transform, width) in references:
   if descriptiveglyphnames:
      target=aliastarget
   else:
      target=ucname(aliastarget)
      ref=ucname(ref)
   if width<0:
      width=outfont[ref].width
   if target in outfont:
      outfont[target].addReference(ref,transform).width=width
   else:
      outfont.createChar(fontforge.unicodeFromName(target),target).addReference(ref,transform).width=width
      if target in freetengenc:
        outfont[target].unicode=freetengenc[target]
      gdh.write('  ' + aliastarget.replace('.', '_') + ' = ps("'+ target + '");\n')

gdh.write('endtable;\n\n')
gdh.close()

## This save and immediate open is a workaround for a bug in FontForge, fixed on April 28, 2011.
outfont.save("TengwarFormalCSUR.sfd")
outfont=fontforge.open("TengwarFormalCSUR.sfd")

## Some systems (OS X 10.6.2) have problems with fonts with nested references.
## So let's un-nest them, making all references directly to the original glyph.
## This is done automatically below, but before that, let's unlink some characters.
## (It's excessive to have each A-tehta be made up of references to the I-tehta.)
if descriptiveglyphnames:
   outfont.selection.select("tehtaA.shift4","tehtaYB.lambeoriginal")
else:
   outfont.selection.select(ucname("tehtaA.shift4"),ucname("tehtaYB.lambeoriginal"))
outfont.unlinkReferences()

def removenestedrefs(char):
   if outfont[char].references==():
      return [(char,psMat.identity())]
   else:
      newrefs=[]
      for (refglyph,transform) in outfont[char].references:
         subrefs=removenestedrefs(refglyph)
         for (newglyph,newtrans) in subrefs:
            newrefs.append((newglyph,psMat.compose(newtrans,transform)))
      return newrefs

for char in outfont:
   if outfont[char].references!=():
      outfont[char].references=tuple(removenestedrefs(char))

## Some users have complained that the font is too small, compared to other fonts. So we scale it 140%:
outfont.selection.all()
outfont.transform(psMat.scale(1.4))

## Old versions of GrCompiler can't handle OS2 version = 4, which is the default in later versions of FontForge.
outfont.os2_version=3

outfont.save("TengwarFormalCSUR.sfd")
outfont=fontforge.open("TengwarFormalCSUR.sfd")

outfont.generate("TengwarFormalCSUR_dumb.ttf")

