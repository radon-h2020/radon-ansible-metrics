import pytest
from ansiblemetrics.playbook.num_included_roles import NumIncludedRoles

script_0 = '- name: Include task list in play\n\tdebug:\n\t\tmsg: hello'
script_2 = '- name: Include task list in play\n\tinclude_role: role1.yaml\n- name: Include task list in ' \
           'play\n\tinclude_role: role2.yaml\n- debug:\n\tmsg: hello '

TEST_DATA = [
    (script_0, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumIncludedRoles(script).count() == expected
