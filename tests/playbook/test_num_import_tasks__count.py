import pytest
from ansiblemetrics.playbook.num_imported_tasks import NumImportedTasks

script_0 = "- name: Some task\n- name: Another task"
script_2 = "- name: Include task list in play\n\timport_tasks: stuff.yaml\n- name: Apply conditional to all imported " \
           "tasks\n\timport_tasks: stuff.yaml\n\twhen: hostvar is defined "

TEST_DATA = [
    (script_0, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumImportedTasks(script).count() == expected
