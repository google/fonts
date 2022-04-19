from fontTools.ttLib import TTFont
from fontTools.otlLib.builder import buildStatTable
from pkg_resources import resource_filename
from google.protobuf import text_format
from collections import OrderedDict
from axisregistry.axes_pb2 import AxisProto
from collections import defaultdict

try:
    from ._version import version as __version__  # type: ignore
except ImportError:
    __version__ = "0.0.0+unknown"


def AxisRegistry():
    registry = {}

    def get_Protobuf_Message(klass, path):
        message = klass()
        with open(path, "rb") as text_data:
            text_format.Merge(text_data.read(), message)
        return message

    def append_AxisMessage(path):
        axis = get_Protobuf_Message(AxisProto, path)
        registry[axis.tag] = axis  # pylint: disable=E1101

    for axis in [
        "casual.textproto",
        "cursive.textproto",
        "fill.textproto",
        "flair.textproto",
        "grade.textproto",
        "italic.textproto",
        "monospace.textproto",
        "optical_size.textproto",
        "slant.textproto",
        "softness.textproto",
        "volume.textproto",
        "weight.textproto",
        "width.textproto",
        "wonky.textproto",
        "x_opaque.textproto",
        "x_transparent_figures.textproto",
        "x_transparent.textproto",
        "y_opaque.textproto",
        "y_transparent_ascender.textproto",
        "y_transparent_descender.textproto",
        "y_transparent_figures.textproto",
        "y_transparent_lowercase.textproto",
        "y_transparent_uppercase.textproto",
    ]:
        append_AxisMessage(resource_filename("axisregistry", "data/" + axis))

    return registry


class NameBuilder:
    def __init__(self, ttFont):
        self.ttFont = ttFont
        self.name_table = self.ttFont["name"]
        self.axis_reg = AxisRegistry()
        self.weights = self.axis_reg["wght"].fallback
        self.family_name = self.ttFont["name"].getBestFamilyName()
        self.subfamily_name = self.ttFont["name"].getBestSubFamilyName()
    
    def is_variable(self):
        return "fvar" in self.ttFont

    def _fvar_dflts(self):
        res = OrderedDict()
        for a in self.ttFont["fvar"].axes:
            # find name and elision
            if a.axisTag in self.axis_reg:
                name = next((f.name for f in self.axis_reg[a.axisTag].fallback if f.value == a.defaultValue), None)
                elided = a.defaultValue == self.axis_reg[a.axisTag].default_value and name not in ["Regular", "Italic"]
            else:
                name = None
                elided = True # since we can't find a name for it, keep it elided
            
            res[a.axisTag] = {
                "value": a.defaultValue,
                "name": name,
                "elided": elided 
            }
        return res

    def build_stat(self, sibling_ttFonts=None):
        print("Building stat table")
        assert self.is_variable(), "not a VF!"
        fallbacks_in_font = self._fallbacks_in_font()
        sibling_font_styles = self._sibling_font_styles(sibling_ttFonts)

        res = []
        # use fontTools build_stat
        # https://github.com/fonttools/fonttools/blob/a293606fc8c88af8510d0688a6a36271ff4ff350/Lib/fontTools/otlLib/builder.py#L2683
        # TODO add linked values
        for axis, fallbacks in fallbacks_in_font.items():
            a = {
                "tag": axis,
                "name": self.axis_reg[axis].display_name,
                "values": []
            }
            for fallback in fallbacks:
                a["values"].append(
                    {
                        "name": fallback.name,
                        "value": fallback.value,
                        # include flags and linked values
                        "flags": 0x2 if fallback.value == self.axis_reg[axis].default_value else 0x0
                    }
                )
            res.append(a)
        
        if sibling_font_styles:
            for axis, fallback in sibling_font_styles:
                a = {
                    "tag": axis,
                    "name": self.axis_reg[axis].name,
                    "values": [
                        {
                            "name": fallback.name,
                            "value": 0,
                            "flags": 0x2 if fallback.value == self.axis_reg[axis].default_value else 0x0
                        }
                    ]
                }
                res.append(a)
        buildStatTable(self.ttFont, res, macNames=False)
    
    def _fallbacks_in_font(self):
        res = defaultdict(list)
        axes_in_font = {a.axisTag: {"min": a.minValue, "max": a.maxValue} for a in self.ttFont["fvar"].axes}
        for axis in self.axis_reg:
            if axis not in axes_in_font:
                continue
            for fallback in self.axis_reg[axis].fallback:
                if fallback.value < axes_in_font[axis]["min"] or fallback.value > axes_in_font[axis]["max"]:
                    continue
                res[axis].append(fallback)
        return res

    def _sibling_font_styles(self, sibling_ttFonts=None):
        if not sibling_ttFonts:
            return
        def name_in_axis_reg(name):
            for a in self.axis_reg:
                for fallback in self.axis_reg[a].fallback:
                    if name == fallback.name:
                        return a, fallback
            return None, None

        res = []
        for sibling_ttFont in sibling_ttFonts:
            name_table = sibling_ttFont["name"]
            tokens = name_table.getBestFamilyName().split() + name_table.getBestSubFamilyName().split()

            fvar_axes_in_font = [a.AxisTag for a in sibling_ttFont["fvar"].axes]

            for token in tokens:
                axis, fallback = name_in_axis_reg(token)
                if not axis or axis in fvar_axes_in_font:
                    continue
                res.append((axis, fallback))
        return res

    def build_name_table(self, family_name=None, style_name=None):
        family_name = family_name if family_name else self.name_table.getBestFamilyName()
        style_name = style_name if style_name else self.name_table.getBestSubFamilyName()
        if self.is_variable():
            return self.build_vf_name_table(family_name)
        return self.build_static_name_table_v1(family_name, style_name)
    
    def build_vf_name_table(self, family_name):
        # VF name table should reflect the 0 origin of the font!
        print("building vf name table")
        style_name = self._vf_style_name()
        self.build_static_name_table(family_name, style_name)
    
    def _vf_style_name(self):
        fvar_dflts = self._fvar_dflts()
        res = []
        for k,v in fvar_dflts.items():
            if v["elided"]:
                continue
            res.append(v["name"])
        return " ".join(res)

    def build_static_name_table(self, family_name, style_name):
        print("building static name table")
        # TODO uniqueID and replace occurences in all records
        # stip mac names
        self.name_table.removeNames(platformID=1)

        names = {}
        is_ribbi = False
        if style_name in ("Regular", "Italic", "Bold", "Bold Italic"):
            is_ribbi = True
        
        if is_ribbi:
            full_name = f"{family_name} {style_name}"
            ps_name = full_name.replace(" ", "")
            names[(1, 3, 1, 0x409)] = family_name
            names[(2, 3, 1, 0x409)] = style_name
            names[(4, 3, 1, 0x409)] = full_name
            names[(6, 3, 1, 0x409)] = ps_name
            for name_id in (16, 17, 21, 22):
                self.name_table.removeNames(nameID=name_id)
        else:
            style_tokens = style_name.split()
            new_family_name = family_name.split()
            is_italic = "Italic" in style_tokens
            for t in style_tokens:
                if t == "Italic":
                    continue
                new_family_name.append(t)
            new_family_name = " ".join(new_family_name)
            new_style_name = "Italic" if is_italic else "Regular"
            full_name = f"{new_family_name} {new_style_name}"
            ps_name = full_name.replace(" ", "")
            
            names[(1, 3, 1, 0x409)] = new_family_name
            names[(2, 3, 1, 0x409)] = new_style_name 
            names[(4, 3, 1, 0x409)] = full_name
            names[(6, 3, 1, 0x409)] = ps_name
            names[(16, 3, 1, 0x409)] = family_name
            names[(17, 3, 1, 0x409)] = style_name
            for name_id in (21, 22):
                self.name_table.removeNames(nameID=name_id)
        
        for k, v in names.items():
            self.name_table.setName(v, *k)

    def build_static_name_table_v1(self, family_name, style_name):
        """Pre VF name tables, this version can only accept wght + ital"""
        print("building static name table")
        non_weight_tokens = []
        tokens = style_name.split()
        for t in tokens:
            if t not in self.weights + ["Italic"]:
                non_weight_tokens.append(t)
        
        family_tokens = family_name.split()
        new_family_name = []
        for t in family_tokens:
            if t in non_weight_tokens:
                continue
            new_family_name.append(t)

        for t in non_weight_tokens:
            new_family_name.append(t)
        
        family_name = " ".join(new_family_name)
        self.build_static_name_table(family_name, style_name)


def main():
    f = TTFont("/Users/marcfoley/Type/upstream_repos/mavenproFont/fonts/variable/MavenPro[wght].ttf")
    namer = NameBuilder(f)
    namer.build_stat()
    namer.build_name_table("Maven Pro Trial")


if __name__ == "__main__":
    main()