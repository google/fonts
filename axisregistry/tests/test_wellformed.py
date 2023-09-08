import pytest
from axisregistry import AxisRegistry
from axisregistry.axes_pb2 import AxisProto

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
        assert field_name in raw_fields, field_name
        assert raw_fields[field_name] is not None, field_name
