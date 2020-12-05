import pytest
from ansiblemetrics.playbook.num_unique_names import NumUniqueNames

script_0 = '---\n- name: logic and comparison\n\thosts: localhost\n\tgather_facts: false\n\tvars:\n\tnum1: ' \
           '10\n\tnum3: 10\n\ttasks:\n\t- name: logic and comparison\n\t\tdebug:\n\t\t\tmsg: "Can you read ' \
           'me?"\n\t\twhen: num1 >= num3 and num1 is even and num2 is not defined\n\t- name: logic and ' \
           'comparison\n\t\tdebug:\n\t\t\tmsg: "Can you read me again?"\n\t\twhen: num3 >= num1 '
script_2 = '- become: false\n\tgather_facts: false\n\thosts: testhost\n\tname: Test vars_prompt ' \
           'confirm\n\ttasks:\n\t- assert:\n\t\t\tthat:\n\t\t\t- input == \'confirm me\'\n\t\tname: null\n\t- ' \
           'debug:\n\t\t\tvar: input\n\tvars_prompt:\n\t- confirm: true\n\t\tname: input '
script_3 = '---\n- name: demo the logic\n\thosts: localhost\n\tgather_facts: false\n\tvars:\n\tnum1: 10\n\tnum3: ' \
           '10\n\ttasks:\n\t- name: logic and comparison 1\n\t\tdebug:\n\t\t\tmsg: "Can you read me?"\n\t\twhen: num1 ' \
           '>= num3 and num1 is even and num2 is not defined\n\t- name: logic and comparison ' \
           '2\n\t\tdebug:\n\t\t\tmsg: "Can you read me again?"\n\t\twhen: num3 >= num1 '


TEST_DATA = [
    (script_0, 0),
    (script_2, 2),
    (script_3, 3)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumUniqueNames(script).count() == expected
