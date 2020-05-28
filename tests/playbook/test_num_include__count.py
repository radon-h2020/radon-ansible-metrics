import pytest
from io import StringIO
from ansiblemetrics.playbook.num_include import NumInclude

#script_include
script_0 = '- name: Include task list in play\n\tinclude_role: role.yaml'
script_1 = '- name: Include a play after another play\n\tinclude: otherplays.yaml\n- name: Include task list in play\n\tinclude_role: role.yaml'

TEST_DATA = [
    (script_0, 0),
    (script_1, 1)
]

@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = NumInclude(script).count()
    script.close()
    assert count == expected