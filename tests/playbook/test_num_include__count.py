import pytest
from ansiblemetrics.playbook.num_includes import NumIncludes

script_0 = '- name: Include task list in play\n\tinclude_role: role.yaml'
script_1 = '- name: Include a play after another play\n\tinclude: otherplays.yaml\n- name: Include task list in ' \
           'play\n\tinclude_role: role.yaml '
script_2 = "- name: Include list in play\n\tansible.builtin.include: stuff.yaml\n- name: Apply conditional to all imported " \
           "tasks\n\tansible.builtin.include: stuff.yaml\n\twhen: hostvar is defined "

TEST_DATA = [
    (script_0, 0),
    (script_1, 1),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumIncludes(script).count() == expected
