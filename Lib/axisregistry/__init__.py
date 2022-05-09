from copy import deepcopy
from fontTools.ttLib import TTFont
from fontTools.otlLib.builder import buildStatTable
from fontTools.varLib.instancer.names import _updateUniqueIdNameRecord
from fontTools.ttLib.tables._f_v_a_r import NamedInstance
from pkg_resources import resource_filename
from google.protobuf import text_format
from collections import OrderedDict
from axisregistry.axes_pb2 import AxisProto
from collections import defaultdict
import logging

try:
    from ._version import version as __version__  # type: ignore
except ImportError:
    __version__ = "0.0.0+unknown"

log = logging.getLogger(__file__)

# TODO we may have more of these. Please note that some applications may not
# implement variable font style linking.
LINKED_VALUES = {
    "wght": {400.0: 700.0},
    "ital": {0.0: 1.0},
}


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


class GFNameBuilder:
    def __init__(self, ttFont, axis_registry=AxisRegistry()):
        self.ttFont = ttFont
        self.name_table = self.ttFont["name"]
        self.axis_reg = axis_registry
        self.weights = [i.name for i in self.axis_reg["wght"].fallback]
        self.v1_styles = self.weights + [
            f"{i} Italic".replace("Regular Italic", "Italic") for i in self.weights
        ]
        self.family_name = self.ttFont["name"].getBestFamilyName()
        self.subfamily_name = self.ttFont["name"].getBestSubFamilyName()

    def is_variable(self):
        return "fvar" in self.ttFont

    def _fvar_dflts(self):
        res = OrderedDict()
        for a in self.ttFont["fvar"].axes:
            # find name and elision
            if a.axisTag in self.axis_reg:
                name = next(
                    (
                        f.name
                        for f in self.axis_reg[a.axisTag].fallback
                        if f.value == a.defaultValue
                    ),
                    None,
                )
                elided = a.defaultValue == self.axis_reg[
                    a.axisTag
                ].default_value and name not in ["Regular", "Italic"]
            else:
                name = None
                elided = True  # since we can't find a name for it, keep it elided

            res[a.axisTag] = {"value": a.defaultValue, "name": name, "elided": elided}
        return res

    def build_stat(self, sibling_ttFonts=None):
        log.info("Building STAT table")
        assert self.is_variable(), "not a VF!"
        fallbacks_in_font = self._fallbacks_in_font()
        sibling_font_styles = self.styles_in_name_table(sibling_ttFonts)
        font_styles = self.styles_in_name_table([self.ttFont])
        nametable = self.ttFont["name"]

        # rm old name table records and STAT table
        if "STAT" in self.ttFont:
            stat = self.ttFont["STAT"]
            axis_values = stat.table.AxisValueArray.AxisValue
            axes = stat.table.DesignAxisRecord.Axis
            for ax in axis_values:
                nametable.removeNames(nameID=ax.ValueNameID)
            for ax in axes:
                nametable.removeNames(nameID=ax.AxisNameID)
            del self.ttFont["STAT"]

        res = []
        # use fontTools build_stat
        # https://github.com/fonttools/fonttools/blob/a293606fc8c88af8510d0688a6a36271ff4ff350/Lib/fontTools/otlLib/builder.py#L2683
        # TODO add linked values
        seen_axes = set()
        for axis, fallbacks in fallbacks_in_font.items():
            seen_axes.add(axis)
            a = {"tag": axis, "name": self.axis_reg[axis].display_name, "values": []}
            for fallback in fallbacks:
                a["values"].append(
                    {
                        "name": fallback.name,
                        "value": fallback.value,
                        # include flags and linked values
                        "flags": 0x2
                        if fallback.value == self.axis_reg[axis].default_value
                        else 0x0,
                    }
                )
                if axis in LINKED_VALUES and fallback.value in LINKED_VALUES[axis]:
                    a["values"][-1]["linkedValue"] = LINKED_VALUES[axis][fallback.value]
            res.append(a)

        if font_styles:
            for axis, fallback in font_styles:
                if axis in seen_axes:
                    continue
                a = {
                    "tag": axis,
                    "name": self.axis_reg[axis].display_name,
                    "values": [
                        {"name": fallback.name, "value": fallback.value, "flags": 0x0}
                    ],
                }
                if axis in LINKED_VALUES and fallback.value in LINKED_VALUES[axis]:
                    a["values"][0]["linkedValue"] = LINKED_VALUES[axis][fallback.value]
                res.append(a)

        if sibling_font_styles:
            for axis, fallback in sibling_font_styles:
                if axis in seen_axes:
                    continue
                value = 0.0
                a = {
                    "tag": axis,
                    "name": self.axis_reg[axis].display_name,
                    "values": [{"name": "Normal", "value": value, "flags": 0x2}],
                }
                if axis in LINKED_VALUES and value in LINKED_VALUES[axis]:
                    a["values"][0]["linkedValue"] = LINKED_VALUES[axis][value]
                res.append(a)
        # TODO, we need to get ordering done
        buildStatTable(self.ttFont, res, macNames=False)

    def _fallbacks_in_font(self):
        res = defaultdict(list)
        axes_in_font = {
            a.axisTag: {"min": a.minValue, "max": a.maxValue}
            for a in self.ttFont["fvar"].axes
        }
        for axis in self.axis_reg:
            if axis not in axes_in_font:
                continue
            for fallback in self.axis_reg[axis].fallback:
                if (
                    fallback.value < axes_in_font[axis]["min"]
                    or fallback.value > axes_in_font[axis]["max"]
                ):
                    continue
                res[axis].append(fallback)
        return res

    def styles_in_name_table(self, sibling_ttFonts=None):
        if not sibling_ttFonts:
            return []

        def name_in_axis_reg(name):
            for a in self.axis_reg:
                for fallback in self.axis_reg[a].fallback:
                    if name == fallback.name:
                        return a, fallback
            return None, None

        res = []
        for sibling_ttFont in sibling_ttFonts:
            name_table = sibling_ttFont["name"]
            tokens = (
                name_table.getBestFamilyName().split()
                + name_table.getBestSubFamilyName().split()
            )

            fvar_axes_in_font = [a.axisTag for a in sibling_ttFont["fvar"].axes]

            for token in tokens:
                axis, fallback = name_in_axis_reg(token)
                if not axis or axis in fvar_axes_in_font:
                    continue
                res.append((axis, fallback))
        return res

    def build_name_table(self, family_name=None, style_name=None, siblings=[]):
        log.info("Building name table")
        family_name = (
            family_name if family_name else self.name_table.getBestFamilyName()
        )
        style_name = (
            style_name if style_name else self.name_table.getBestSubFamilyName()
        )
        if self.is_variable():
            return self.build_vf_name_table(family_name, siblings=siblings)
        return self.build_static_name_table_v1(family_name, style_name)

    def build_vf_name_table(self, family_name, siblings=[]):
        # VF name table should reflect the 0 origin of the font!
        assert self.is_variable(), "Not a VF!"
        style_name = self._vf_style_name()
        # if there are sibling fonts and the style name isn't wght+ital, use the v1 static method
        if siblings and style_name not in self.v1_styles:
            self.build_static_name_table_v1(family_name, style_name)
        else:
            self.build_static_name_table(family_name, style_name)

        # set nameID25
        font_styles = self.styles_in_name_table([self.ttFont])
        if font_styles:
            vf_ps = family_name.replace(" ", "") + "".join(
                [s[1].name for s in font_styles]
            )
        else:
            vf_ps = family_name.replace(" ", "")
        self.ttFont["name"].setName(vf_ps, 25, 3, 1, 0x409)

    def _vf_style_name(self):
        fvar_dflts = self._fvar_dflts()
        res = []
        for k, v in fvar_dflts.items():
            if v["elided"]:
                continue
            res.append(v["name"])

        font_styles = self.styles_in_name_table([self.ttFont])
        for _, s in font_styles:
            if s.name in res:
                continue
            res.append(s.name)
        name = " ".join(res).replace("Regular Italic", "Italic")
        log.debug(f"Built VF style name: '{name}'")
        return name

    def build_fvar_instances(self, axis_dflts={}):
        """Replace a variable font's fvar instances with a set of new instances
        which conform to the Google Fonts instance spec:
        https://github.com/googlefonts/gf-docs/tree/main/Spec#fvar-instances
        Args:
            ttFont: a TTFont instance
        """
        assert self.is_variable(), "Not a VF!"
        log.info("Building fvar instances")
        fvar = self.ttFont["fvar"]
        nametable = self.ttFont["name"]

        # rm old fvar subfamily and ps name records
        for inst in fvar.instances:
            nametable.removeNames(nameID=inst.subfamilyNameID)
            if inst.postscriptNameID != 65535:
                nametable.removeNames(nameID=inst.postscriptNameID)

        fvar_dflts = self._fvar_dflts()
        if not axis_dflts:
            axis_dflts = {k: v["value"] for k, v in fvar_dflts.items()}

        is_italic = "Italic" in self.subfamily_name
        is_roman_and_italic = any(a for a in ("slnt", "ital") if a in fvar_dflts)

        if "wght" not in fvar_dflts:
            raise NotImplementedError()

        ital_axis = next((a for a in fvar.axes if a.axisTag == "ital"), None)
        slnt_axis = next((a for a in fvar.axes if a.axisTag == "slnt"), None)

        fallbacks = self._fallbacks_in_font()
        wght_fallbacks = fallbacks["wght"]

        def gen_instances(is_italic):
            results = []
            for fallback in wght_fallbacks:
                name = (
                    fallback.name
                    if not is_italic
                    else f"{fallback.name} Italic".strip()
                )
                name = name.replace("Regular Italic", "Italic")

                coordinates = {k: v for k, v in axis_dflts.items()}
                coordinates["wght"] = fallback.value
                if is_italic:
                    if ital_axis:
                        coordinates["ital"] = ital_axis.minValue
                    elif slnt_axis:
                        coordinates["slnt"] = slnt_axis.minValue

                inst = NamedInstance()
                inst.subfamilyNameID = nametable.addName(name)
                inst.coordinates = coordinates
                log.debug(f"Adding fvar instance: {name}: {coordinates}")
                results.append(inst)
            return results

        instances = []
        if is_roman_and_italic:
            for bool_ in (False, True):
                instances += gen_instances(is_italic=bool_)
        elif is_italic:
            instances += gen_instances(is_italic=True)
        else:
            instances += gen_instances(is_italic=False)
        fvar.instances = instances

    def build_static_name_table(self, family_name, style_name):
        # TODO replace occurences in all records
        # stip mac names
        self.name_table.removeNames(platformID=1)

        names = {}
        is_ribbi = False
        if style_name in ("Regular", "Italic", "Bold", "Bold Italic"):
            is_ribbi = True

        if is_ribbi:
            full_name = f"{family_name} {style_name}"
            ps_name = f"{family_name}-{style_name}".replace(" ", "")
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
                if t in ["Regular", "Italic"]:
                    continue
                new_family_name.append(t)
            new_family_name = " ".join(new_family_name)
            new_style_name = "Italic" if is_italic else "Regular"
            full_name = f"{family_name} {style_name}"
            ps_name = f"{family_name}-{style_name}".replace(" ", "")

            names[(1, 3, 1, 0x409)] = new_family_name
            names[(2, 3, 1, 0x409)] = new_style_name
            names[(4, 3, 1, 0x409)] = full_name
            names[(6, 3, 1, 0x409)] = ps_name
            names[(16, 3, 1, 0x409)] = family_name
            names[(17, 3, 1, 0x409)] = style_name
            for name_id in (21, 22):
                self.name_table.removeNames(nameID=name_id)

        names[(3, 3, 1, 0x409)] = _updateUniqueIdNameRecord(
            self.ttFont, {k[0]: v for k, v in names.items()}, (3, 1, 0x409)
        )
        for k, v in names.items():
            log.debug(f"Adding name record {k}: {v}")
            self.name_table.setName(v, *k)

    def build_static_name_table_v1(self, family_name, style_name):
        """Pre VF name tables, this version can only accept wght + ital"""
        non_weight_tokens = []
        v1_tokens = []
        tokens = style_name.split()
        for t in tokens:
            if t not in self.weights + ["Italic"]:
                non_weight_tokens.append(t)
            else:
                v1_tokens.append(t)

        family_tokens = family_name.split()
        new_family_name = []
        for t in family_tokens:
            if t in non_weight_tokens or t in new_family_name:
                continue
            new_family_name.append(t)
        for t in non_weight_tokens:
            new_family_name.append(t)

        family_name = " ".join(new_family_name)
        style_name = " ".join(v1_tokens).replace("Regular Italic", "Italic").strip()
        log.debug(f"New family name: {family_name}")
        log.debug(f"New style name: {style_name}")
        self.build_static_name_table(family_name, style_name)
