import pytest
from io import StringIO
from ansiblemetrics.general.text_entropy import TextEntropy

#script_entropy
script_0 = "- hosts"
script_273 = "- hosts: all\n\troles:\n\t- common\n\n- hosts: dbservers\n\troles:\n\t- db\n\t- web"

TEST_DATA = [
    (script_0, 0),
    (script_273, 2.73)
]

@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = TextEntropy(script).count()
    script.close()
    assert count == expected