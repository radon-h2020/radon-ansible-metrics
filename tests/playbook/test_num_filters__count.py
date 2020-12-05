import pytest
from ansiblemetrics.playbook.num_filters import NumFilters

script_0_1 = '- hosts: all\n\tvars:\n\t\tcontents: "static content"\n\n\ttasks:\n\t\t- debug: msg="the value of ' \
             'foo.txt is {{ contents }}" '
script_0_2 = 'tasks:\n\t- shell: cat /some/path/to/multidoc-file.yaml\n\t\tregister: result\n\t- debug:\n\t\t\tmsg: ' \
             '\'{{ item }}\'\n\t\tloop: \'{{ result.stdout || list }}\'\t# 2 filters '
script_2 = 'tasks:\n\t- shell: cat /some/path/to/multidoc-file.yaml\n\t\tregister: result\n\t- debug:\n\t\t\tmsg: \'{' \
           '{ item }}\'\n\t\tloop: \'{{ result.stdout | from_yaml_all | list }}\'\t# 2 filters '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumFilters(script).count() == expected

