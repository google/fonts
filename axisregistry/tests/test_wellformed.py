import re
import sys

import pytest
from axisregistry import AxisRegistry
from axisregistry.axes_pb2 import AxisProto

if sys.version_info < (3, 10):
    from importlib_resources import files
else:
    from importlib.resources import files

registry = AxisRegistry()

OPTIONAL_FIELDS = ["illustration_url", "is_parametric"]


@pytest.mark.parametrize("axis_tag", registry.keys())
def test_proto_wellformed(axis_tag):
    axis = registry[axis_tag]
    raw_fields = dict([(k.name, v) for k, v in axis.ListFields()])
    for field in AxisProto.DESCRIPTOR.fields:
        field_name = field.name
        if field_name in OPTIONAL_FIELDS:
            continue
        assert (
            field_name in raw_fields
        ), f"Non-optional field {field_name} is missing in {axis_tag}"
        assert raw_fields[field_name] is not None, field_name


proto_files = [
    file
    for file in files("axisregistry.data").iterdir()
    if file.name.endswith(".textproto")
]


@pytest.mark.parametrize("proto_file", proto_files)
def test_proto_multiline_string(proto_file):
    with open(proto_file, "r") as f:
        content = f.read()
    # Check for multiline strings which do not have a space either at the
    # end of the line or at the beginning of the next line
    pattern = re.compile(r'".*\S"\n\s*"\S+')
    matches = pattern.findall(content)
    if matches:
        matches = [re.sub(r'"\n\s+"', "", match) for match in matches]
    # Assert that there are no such matches
    assert (
        not matches
    ), f"Badly-spaced multiline strings found in {proto_file.name}: {', '.join(matches)}"
