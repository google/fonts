from axisregistry import AxisRegistry


def test_AxisRegistry():
    registry = AxisRegistry()
    assert 'GRAD' in registry.keys()
    assert 'message' in registry['GRAD']
    assert 'fallbacks' in registry['GRAD']
    for axis_tag in registry.keys():
        assert len(axis_tag) == 4
        for f in range(len(registry[axis_tag]["message"].fallback)):
            fallback = registry[axis_tag]["message"].fallback[f]

            # fallback names should not be space-separated.
            # (see: https://github.com/googlefonts/axisregistry/issues/7)
            assert ' ' not in fallback.name
