import pytest
from io import StringIO
from ansiblemetrics.general.lines_code import LinesCode

# scripts_loc
script_8 = '---\n- hosts: localhost\n\n\ttasks:\n\t- name: task 1    # This is the first task\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml\n\n# This is the second task\n\t- name: task 2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml'

TEST_DATA = [
    (script_8, 8)
]

@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = LinesCode(script).count()
    script.close()
    assert count == expected