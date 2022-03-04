from axisregistry import AxisRegistry


def test_AxisRegistry():
    registry = AxisRegistry()
    assert 'GRAD' in registry.keys()
    assert 'message' in registry['GRAD']
    assert 'fallbacks' in registry['GRAD']
    for axis_tag in registry.keys():
        assert len(axis_tag) == 4
