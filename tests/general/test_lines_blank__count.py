import pytest
from ansiblemetrics.general.lines_blank import LinesBlank

script_0 = '---\n- hosts: localhost\n\ttasks:\n\t- name: task 1'
script_2 = '---\n- hosts: localhost\n\n\ttasks:\n\t- name: task 1    # This is the first ' \
           'task\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml\n\n# This is the second task\n\t- name: task ' \
           '2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml '

TEST_DATA = [
    (script_0, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert LinesBlank(script).count() == expected
