import pytest
from ansiblemetrics.general.num_math_operations import NumMathOperations

script_0 = '- name: test play\n\thosts: all\n\n\ttasks:\n\n\t\t\t- shell: cat /etc/motd\n\t\t\t\tregister: ' \
           'motd_contents\n\n\t\t\t- shell: echo "motd contains the word hi"\n\t\t\t\twhen: ' \
           'motd_contents.stdout.find(\'hi\') != -1 '
script_5 = '- hosts: loc\n\ttasks:\n\t- debug:\n\t\t\tmsg: "addition{{ 4 + 3 }}"\n\t- debug:\n\t\t\tmsg: "subtraction ' \
           '{{ 4 - 3 }}"\n\t- debug:\n\t\t\tmsg: "multiplication {{ 4 * 3 }}"\n\t- debug:\n\t\t\tmsg: "Modulo ' \
           'operation {{ 7 % 4}}"\n\t- debug:\n\t\t\tmsg: "floating division {{ 4 / 3}}" '

TEST_DATA = [
    (script_0, 0),
    (script_5, 5)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumMathOperations(script).count() == expected
