from pkg_resources import resource_filename
from google.protobuf import text_format

from axisregistry.axes_pb2 import AxisProto

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
        axis_dict = {"message": get_Protobuf_Message(AxisProto, path),
                     "fallbacks": {}}
        for fb in axis_dict["message"].fallback:  # pylint: disable=E1101
            axis_dict["fallbacks"][fb.name] = fb.value
        registry[axis_dict["message"].tag] = axis_dict  # pylint: disable=E1101

    for axis in ["casual.textproto",
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
                 "y_transparent_uppercase.textproto"]:
        append_AxisMessage(resource_filename('axisregistry', 'data/' + axis))

    return registry
