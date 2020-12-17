import pytest
from ansiblemetrics.playbook.num_included_tasks import NumIncludedTasks

script_0 = '- name: Include task list in play\n\tdebug:\n\t\tmsg: task1'
script_2 = '- name: Include task list in play\n\tinclude_tasks: stuff.yaml\n\n- debug:\n\t\tmsg: task10\n\n- name: ' \
           'Apply tags to tasks within included file\n\tinclude_tasks:\n\t\tfile: ' \
           'install.yml\n\t\tapply:\n\t\t\ttags:\n\t\t\t\t- install '

TEST_DATA = [
    (script_0, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumIncludedTasks(script).count() == expected
