from copy import deepcopy
from fontTools.ttLib import TTFont
from fontTools.misc.testTools import getXML
from fontTools.otlLib.builder import buildStatTable
from fontTools.varLib.instancer.names import _updateUniqueIdNameRecord, NameID
from fontTools.ttLib.tables._f_v_a_r import NamedInstance
from pkg_resources import resource_filename
from google.protobuf import text_format
from collections import OrderedDict
from axisregistry.axes_pb2 import AxisProto
from collections import defaultdict
from itertools import chain
import logging
from glob import glob
import os

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

# Static font styles. The GF api only support the following static font styles
GF_STATIC_STYLES = OrderedDict(
    [
        ("Thin", 100),
        ("ExtraLight", 200),
        ("Light", 300),
        ("Regular", 400),
        ("Medium", 500),
        ("SemiBold", 600),
        ("Bold", 700),
        ("ExtraBold", 800),
        ("Black", 900),
        ("Thin Italic", 100),
        ("ExtraLight Italic", 200),
        ("Light Italic", 300),
        ("Italic", 400),
        ("Medium Italic", 500),
        ("SemiBold Italic", 600),
        ("Bold Italic", 700),
        ("ExtraBold Italic", 800),
        ("Black Italic", 900),
    ]
)


def load_protobuf(klass, path):
    message = klass()
    with open(path, "rb") as text_data:
        text_format.Merge(text_data.read(), message)
    return message


class AxisRegistry:
    def __init__(self, fp=resource_filename("axisregistry", "data")):
        axis_fps = [fp for fp in glob(os.path.join(fp, "*.textproto"))]
        self._data = {}
        for fp in axis_fps:
            axis = load_protobuf(AxisProto, fp)
            self._data[axis.tag] = axis

    def __getitem__(self, k):
        return self._data[k]

    def __iter__(self):
        for i in self._data.keys():
            yield i

    def keys(self):
        return self._data.keys()

    def items(self):
        return self._data.items()

    def get_fallback(self, name):
        for a in self:
            for fallback in self[a].fallback:
                if name == fallback.name:
                    return a, fallback
        return None, None

    def fallbacks_in_fvar(self, ttFont):
        res = defaultdict(list)
        axes_in_font = {
            a.axisTag: {"min": a.minValue, "max": a.maxValue}
            for a in ttFont["fvar"].axes
        }
        for axis in axes_in_font:
            if axis not in self.keys():
                log.warn(f"Axis {axis} not found in GF Axis Registry!")
                continue
            for fallback in self[axis].fallback:
                if (
                    fallback.value < axes_in_font[axis]["min"]
                    or fallback.value > axes_in_font[axis]["max"]
                ):
                    continue
                res[axis].append(fallback)
        return res

    def fallbacks_in_name_table(self, ttFont):
        res = []
        name_table = ttFont["name"]
        tokens = (
            name_table.getBestFamilyName().split()[1:]
            + name_table.getBestSubFamilyName().split()
        )
        fvar_axes_in_font = [a.axisTag for a in ttFont["fvar"].axes]
        for token in tokens:
            axis, fallback = axis_registry.get_fallback(token)
            if any([not axis, axis in fvar_axes_in_font, fallback in res]):
                continue
            res.append((axis, fallback))
        return res

    def fallback_for_value(self, axis_tag, value):
        if axis_tag in axis_registry:
            return next(
                (f for f in axis_registry[axis_tag].fallback if f.value == value),
                None,
            )
        return None


axis_registry = AxisRegistry()
# sort user axes by alphabetical order and append presorted registered axes
AXIS_ORDER = sorted([i for i in axis_registry if i.isupper()]) + [
    "opsz",
    "wdth",
    "wght",
    "ital",
    "slnt",
]


def is_variable(ttFont):
    return "fvar" in ttFont


def _fvar_dflts(ttFont):
    res = OrderedDict()
    for a in ttFont["fvar"].axes:
        fallback = axis_registry.fallback_for_value(a.axisTag, a.defaultValue)
        if fallback:
            name = fallback.name
            elided = fallback.value == axis_registry[
                a.axisTag
            ].default_value and name not in ["Regular", "Italic", "14pt"]
        elif a.axisTag == "opsz":
            name = f"{int(a.defaultValue)}pt"
            elided = False
        else:
            name = None
            elided = True  # since we can't find a name for it, keep it elided
        res[a.axisTag] = {"value": a.defaultValue, "name": name, "elided": elided}
    return res


def build_stat(ttFont, sibling_ttFonts=[]):
    log.info("Building STAT table")
    assert is_variable(ttFont), "not a VF!"
    fallbacks_in_fvar = axis_registry.fallbacks_in_fvar(ttFont)
    fallbacks_in_siblings = list(
        chain.from_iterable(
            axis_registry.fallbacks_in_name_table(f) for f in sibling_ttFonts
        )
    )
    fallbacks_in_names = axis_registry.fallbacks_in_name_table(ttFont)
    nametable = ttFont["name"]
    fvar = ttFont["fvar"]

    # rm old STAT table and associated name table records
    fvar_instance_nameids = set(i.subfamilyNameID for i in fvar.instances)
    fvar_axis_nameids = set(a.axisNameID for a in fvar.axes)
    fvar_nameids = fvar_axis_nameids | fvar_instance_nameids
    # These NameIDs are required for applications to work correctly so
    # they cannot be deleted.
    # https://learn.microsoft.com/en-us/typography/opentype/spec/name
    keep_nameids = set(range(26)) | fvar_nameids
    if "STAT" in ttFont:
        stat = ttFont["STAT"]
        if stat.table.AxisValueCount > 0:
            axis_values = stat.table.AxisValueArray.AxisValue
            for ax in axis_values:
                if ax.ValueNameID not in keep_nameids:
                    nametable.removeNames(nameID=ax.ValueNameID)
        if stat.table.DesignAxisCount > 0:
            axes = stat.table.DesignAxisRecord.Axis
            for ax in axes:
                if ax.AxisNameID not in keep_nameids:
                    nametable.removeNames(nameID=ax.AxisNameID)
        del ttFont["STAT"]

    res = []
    # use fontTools build_stat. Link contains function params and usage example
    # https://github.com/fonttools/fonttools/blob/a293606fc8c88af8510d0688a6a36271ff4ff350/Lib/fontTools/otlLib/builder.py#L2683
    seen_axes = set()
    for axis, fallbacks in fallbacks_in_fvar.items():
        seen_axes.add(axis)
        a = {"tag": axis, "name": axis_registry[axis].display_name, "values": []}
        for fallback in fallbacks:
            a["values"].append(
                {
                    "name": fallback.name,
                    "value": fallback.value,
                    # include flags and linked values
                    "flags": 0x2
                    if fallback.value == axis_registry[axis].default_value
                    else 0x0,
                }
            )
            if axis in LINKED_VALUES and fallback.value in LINKED_VALUES[axis]:
                linked_value = LINKED_VALUES[axis][fallback.value]
                if any(f.value == linked_value for f in fallbacks):
                    a["values"][-1]["linkedValue"] = linked_value
        res.append(a)

    for axis, fallback in fallbacks_in_names:
        if axis in seen_axes:
            continue
        a = {
            "tag": axis,
            "name": axis_registry[axis].display_name,
            "values": [{"name": fallback.name, "value": fallback.value, "flags": 0x0}],
        }
        if axis in LINKED_VALUES and fallback.value in LINKED_VALUES[axis]:
            linked_value = LINKED_VALUES[axis][fallback.value]
            a["values"][0]["linkedValue"] = linked_value
        res.append(a)

    for axis, fallback in fallbacks_in_siblings:
        if axis in seen_axes:
            continue
        elided_value = axis_registry[axis].default_value
        elided_fallback = axis_registry.fallback_for_value(axis, elided_value)
        a = {
            "tag": axis,
            "name": axis_registry[axis].display_name,
            "values": [
                {"name": elided_fallback.name, "value": elided_value, "flags": 0x2}
            ],
        }
        if axis in LINKED_VALUES and elided_value in LINKED_VALUES[axis]:
            a["values"][0]["linkedValue"] = LINKED_VALUES[axis][elided_value]
        res.append(a)
    buildStatTable(ttFont, res, macNames=False)


def build_name_table(ttFont, family_name=None, style_name=None, siblings=[]):
    from fontTools.varLib.instancer import setRibbiBits

    log.info("Building name table")
    name_table = ttFont["name"]
    family_name = family_name if family_name else name_table.getBestFamilyName()
    style_name = style_name if style_name else name_table.getBestSubFamilyName()
    if is_variable(ttFont):
        build_vf_name_table(ttFont, family_name, siblings=siblings)
    else:
        build_static_name_table_v1(ttFont, family_name, style_name)

    # Set bits
    style_name = name_table.getBestSubFamilyName()
    # usWeightClass
    weight_seen = False
    for weight in sorted(GF_STATIC_STYLES, key=lambda k: len(k), reverse=True):
        if weight in style_name:
            weight_seen = True
            ttFont["OS/2"].usWeightClass = GF_STATIC_STYLES[weight]
            break
    if not weight_seen:
        log.warning(
            f"No known weight found for stylename {style_name}. Cannot set OS2.usWeightClass"
        )
    setRibbiBits(ttFont)


def _fvar_instance_collisions(ttFont, siblings=[]):
    """Check if a font family is going to have colliding fvar instances.

    Collision occur when a family has has 2+ roman styles or 2+ italic
    styles."""

    def is_italic(font):
        return font["post"].italicAngle != 0.0

    family_styles = [is_italic(f) for f in siblings + [ttFont]]

    return len(family_styles) != len(set(family_styles))


def build_vf_name_table(ttFont, family_name, siblings=[]):
    # VF name table should reflect the 0 origin of the font!
    assert is_variable(ttFont), "Not a VF!"
    style_name = _vf_style_name(ttFont, family_name)
    if _fvar_instance_collisions(ttFont, siblings):
        build_static_name_table_v1(ttFont, family_name, style_name)
    else:
        build_static_name_table(ttFont, family_name, style_name)
    build_variations_ps_name(ttFont, family_name)


def build_variations_ps_name(ttFont, family_name=None):
    assert is_variable(ttFont), "Not a VF!"
    if not family_name:
        family_name = ttFont["name"].getBestFamilyName()
    font_styles = axis_registry.fallbacks_in_name_table(ttFont)
    if font_styles:
        vf_ps = family_name.replace(" ", "") + "".join(
            [
                fallback.name
                for _, fallback in font_styles
                if fallback.name not in family_name
            ]
        )
    else:
        vf_ps = family_name.replace(" ", "")
    ttFont["name"].setName(vf_ps, NameID.VARIATIONS_POSTSCRIPT_NAME_PREFIX, 3, 1, 0x409)


def _vf_style_name(ttFont, family_name):
    fvar_dflts = _fvar_dflts(ttFont)
    res = []
    for axis_name in AXIS_ORDER:
        if axis_name not in fvar_dflts:
            continue
        value = fvar_dflts[axis_name]
        if not value["elided"]:
            res.append(value["name"])

    family_name_tokens = family_name.split()
    font_styles = axis_registry.fallbacks_in_name_table(ttFont)
    for _, fallback in font_styles:
        if fallback.name not in res and fallback.name not in family_name_tokens:
            res.append(fallback.name)

    name = " ".join(res).replace("Regular Italic", "Italic")
    log.debug(f"Built VF style name: '{name}'")
    return name


def build_fvar_instances(ttFont, axis_dflts={}):
    """Replace a variable font's fvar instances with a set of new instances
    which conform to the Google Fonts instance spec:
    https://github.com/googlefonts/gf-docs/tree/main/Spec#fvar-instances
    """
    assert is_variable(ttFont), "Not a VF!"
    log.info("Building fvar instances")
    fvar = ttFont["fvar"]
    name_table = ttFont["name"]
    style_name = name_table.getBestSubFamilyName()

    # Protect name IDs which are shared with the STAT table
    stat_nameids = []
    if "STAT" in ttFont:
        if ttFont["STAT"].table.AxisValueCount > 0:
            stat_nameids.extend(
                av.ValueNameID for av in ttFont["STAT"].table.AxisValueArray.AxisValue
            )
        if ttFont["STAT"].table.DesignAxisCount > 0:
            stat_nameids.extend(
                av.AxisNameID for av in ttFont["STAT"].table.DesignAxisRecord.Axis
            )

    # rm old fvar subfamily and ps name records
    for inst in fvar.instances:
        if inst.subfamilyNameID not in [2, 17] + stat_nameids:
            name_table.removeNames(nameID=inst.subfamilyNameID)
        if inst.postscriptNameID not in [65535, 6]:
            name_table.removeNames(nameID=inst.postscriptNameID)

    fvar_dflts = _fvar_dflts(ttFont)
    if not axis_dflts:
        axis_dflts = {k: v["value"] for k, v in fvar_dflts.items()}

    is_italic = "Italic" in style_name
    is_roman_and_italic = any(a for a in ("slnt", "ital") if a in fvar_dflts)

    fallbacks = axis_registry.fallbacks_in_fvar(ttFont)
    # some families may not have a wght axis e.g
    # https://fonts.google.com/specimen/League+Gothic
    # these families just have a single weight which is Regular
    if "wght" not in fvar_dflts:
        fallback = next(
            (f for f in axis_registry["wght"].fallback if f.value == 400.0), None
        )
        fallbacks["wght"] = [fallback]

    wght_fallbacks = fallbacks["wght"]

    ital_axis = next((a for a in fvar.axes if a.axisTag == "ital"), None)
    slnt_axis = next((a for a in fvar.axes if a.axisTag == "slnt"), None)

    def gen_instances(is_italic):
        results = []
        for fallback in wght_fallbacks:
            name = fallback.name if not is_italic else f"{fallback.name} Italic".strip()
            name = name.replace("Regular Italic", "Italic")

            coordinates = {k: v for k, v in axis_dflts.items()}
            if "wght" in fvar_dflts:
                coordinates["wght"] = fallback.value
            if is_italic:
                if ital_axis:
                    coordinates["ital"] = ital_axis.minValue
                elif slnt_axis:
                    coordinates["slnt"] = slnt_axis.minValue

            inst = NamedInstance()
            inst.subfamilyNameID = name_table.addName(name)
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


def build_static_name_table(ttFont, family_name, style_name):
    # stip mac names
    name_table = ttFont["name"]
    name_table.removeNames(platformID=1)
    existing_name = ttFont["name"].getBestFamilyName()
    removed_names = {}

    names = {}
    is_ribbi = (
        True if style_name in ("Regular", "Italic", "Bold", "Bold Italic") else False
    )
    if is_ribbi:
        full_name = f"{family_name} {style_name}"
        ps_name = f"{family_name}-{style_name}".replace(" ", "")
        names[(NameID.FAMILY_NAME, 3, 1, 0x409)] = family_name
        names[(NameID.SUBFAMILY_NAME, 3, 1, 0x409)] = style_name
        names[(NameID.FULL_FONT_NAME, 3, 1, 0x409)] = full_name
        names[(NameID.POSTSCRIPT_NAME, 3, 1, 0x409)] = ps_name
        for name_id in (
            NameID.TYPOGRAPHIC_FAMILY_NAME,
            NameID.TYPOGRAPHIC_SUBFAMILY_NAME,
            21,
            22,
        ):
            removed_names[name_id] = name_table.getDebugName(name_id)
            name_table.removeNames(nameID=name_id)
    else:
        style_tokens = style_name.split()
        new_family_name = family_name.split()
        is_italic = "Italic" in style_tokens
        for t in style_tokens:
            if t in ["Regular", "Italic"] or t in new_family_name:
                continue
            new_family_name.append(t)
        new_family_name = " ".join(new_family_name)
        new_style_name = "Italic" if is_italic else "Regular"
        full_name = f"{family_name} {style_name}"
        ps_name = f"{family_name}-{style_name}".replace(" ", "")

        names[(NameID.FAMILY_NAME, 3, 1, 0x409)] = new_family_name
        names[(NameID.SUBFAMILY_NAME, 3, 1, 0x409)] = new_style_name
        names[(NameID.FULL_FONT_NAME, 3, 1, 0x409)] = full_name
        names[(NameID.POSTSCRIPT_NAME, 3, 1, 0x409)] = ps_name
        names[(NameID.TYPOGRAPHIC_FAMILY_NAME, 3, 1, 0x409)] = family_name
        names[(NameID.TYPOGRAPHIC_SUBFAMILY_NAME, 3, 1, 0x409)] = style_name
        # we do not use WWS names since we use the RIBBI naming schema
        for name_id in (21, 22):
            removed_names[name_id] = name_table.getDebugName(name_id)
            name_table.removeNames(nameID=name_id)

    # If STAT table was using any removed names, add then back with a new ID
    if "STAT" in ttFont and removed_names:
        if ttFont["STAT"].table.AxisValueArray:
            for av in ttFont["STAT"].table.AxisValueArray.AxisValue:
                if av.ValueNameID in removed_names:
                    av.ValueNameID = name_table.addMultilingualName(
                        {"en": removed_names[av.ValueNameID]}
                    )
        for av in ttFont["STAT"].table.DesignAxisRecord.Axis:
            if av.AxisNameID in removed_names:
                av.AxisNameID = name_table.addMultilingualName(
                    {"en": removed_names[av.AxisNameID]}
                )

    names[(NameID.UNIQUE_FONT_IDENTIFIER, 3, 1, 0x409)] = _updateUniqueIdNameRecord(
        ttFont, {k[0]: v for k, v in names.items()}, (3, 1, 0x409)
    )
    for k, v in names.items():
        log.debug(f"Adding name record {k}: {v}")
        name_table.setName(v, *k)

    # Replace occurences of old family name in untouched records
    skip_ids = [i.numerator for i in NameID]
    for r in ttFont["name"].names:
        if r.nameID in skip_ids:
            continue
        current = r.toUnicode()
        if existing_name not in current:
            continue
        if " " not in current:
            replacement = current.replace(existing_name, family_name).replace(" ", "")
        else:
            replacement = current.replace(existing_name, family_name)
        ttFont["name"].setName(
            replacement, r.nameID, r.platformID, r.platEncID, r.langID
        )


def build_static_name_table_v1(ttFont, family_name, style_name):
    """Pre VF name tables, this version can only accept wght + ital"""
    non_weight_tokens = []
    v1_tokens = []
    tokens = style_name.split()
    for t in tokens:
        if t not in GF_STATIC_STYLES:
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
    style_name = style_name or "Regular"
    log.debug(f"New family name: {family_name}")
    log.debug(f"New style name: {style_name}")
    build_static_name_table(ttFont, family_name, style_name)


def build_filename(ttFont):
    name_table = ttFont["name"]
    family_name = name_table.getBestFamilyName()
    style_name = name_table.getBestSubFamilyName()
    _, ext = os.path.splitext(ttFont.reader.file.name)
    if is_variable(ttFont):
        is_italic = "Italic" in style_name
        axes = _fvar_dflts(ttFont).keys()
        axes = sorted([a for a in axes if a.isupper()]) + sorted(
            [a for a in axes if a.islower()]
        )
        if is_italic:
            return f"{family_name}-Italic[{','.join(axes)}]{ext}".replace(" ", "")
        return f"{family_name}[{','.join(axes)}]{ext}".replace(" ", "")
    return f"{family_name}-{style_name}{ext}".replace(" ", "")


def dump(table, ttFont=None):
    return "\n".join(getXML(table.toXML, ttFont))
