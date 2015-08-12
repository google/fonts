# github.com/google/fonts.git repo trivia

## Duplicated fonts

There are some similarly named pairs of directories which each have identically named font files. 
These files are redundant, and exist following the renaming of a family.
The initial directories are kept so that people already using that initial name can continue to do so. 
They are no longer listed in the main www.google.com/fonts directory, but the files exist in this repo since they are still served via the Google Fonts API. 

- `ofl/mrbedford` and `ofl/mrbedfort` contain `MrBedfort-Regular.ttf`
- `ofl/mrssaintdelafield` and `ofl/misssaintdelafield` contain `MrsSaintDelafield-Regular.ttf`
- `ofl/siamreap` and `ofl/siemreap` contain `Siemreap.ttf`
- `ofl/terminaldosis` and `ofl/dosis` contain the same files (renamed) and `ofl/terminaldosislight` contain `TerminalDosis-Light.ttf`
