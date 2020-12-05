import pytest
from ansiblemetrics.playbook.num_prompts import NumPrompts

script_0 = '- name: An example pool playbook\n\thosts: bigip\n\tconnection: local\n\n\tvars_prompt:\n\t\t- name: ' \
           '"username"\n '
script_2 = '- name: An example pool playbook\n\thosts: bigip\n\tconnection: local\n\n\tvars_prompt:\n\t\t- name: ' \
           '"username"\n\t\t\tprompt: "Enter BIG-IP username"\n\t\t\tprivate: yes\n\t\t- name: ' \
           '"password"\n\t\t\tprompt: "Enter BIG-IP password"\n\t\t\tprivate: yes\n\n\ttasks:\n\t\t- name: Create web ' \
           'servers pool\n\t\t\tbigip_pool:\n\t\t\t\tname: web-servers\n\t\t\t\tlb_method: ' \
           'ratio-member\n\t\t\t\tpassword: "{{ password }}"\n\t\t\t\tserver: 10.1.1.4\n\t\t\t\tuser: "{{ username ' \
           '}}"\n\t\t\t\tvalidate_certs: no '
script_3 = '- hosts: all\n\tremote_user: root\n\n\tvars:\n\t\tfrom: "camelot"\n\n\tvars_prompt:\n\t\t- name: ' \
           '"name"\n\t\t\tprompt: "what is your name?"\n\t\t- name: "quest"\n\t\t\tprompt: "what is your ' \
           'quest?"\n\t\t- name: "favcolor"\n\t\t\tprompt: "what is your favorite color?" '

TEST_DATA = [
    (script_0, 0),
    (script_2, 2),
    (script_3, 3)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumPrompts(script).count() == expected
