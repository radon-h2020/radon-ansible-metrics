import ansiblemetrics.utils as utils


def test_all_keys():
    d = {"keyA": {"keyB": "valueB"}, "keyC": ["valueC1", "valueC2"], "keyD": "hello world"}
    keys = utils.all_keys(d)
    assert len(keys) == 4
    assert "keyA" in keys
    assert "keyB" in keys
    assert "keyC" in keys
    assert "keyD" in keys


def test_all_values():
    d = {"keyA": {"keyB": "valueB"}, "keyC": ["valueC1", "valueC2"], "keyD": "hello world"}
    values = utils.all_values(d)
    assert len(values) == 4
    assert "valueB" in values
    assert "valueC1" in values
    assert "valueC2" in values
    assert "hello world" in values
