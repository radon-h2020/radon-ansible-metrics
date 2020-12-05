import pytest
from ansiblemetrics.playbook.num_vars import NumVars

script_vars_null = '- name: a name\n\tvars:'
script_0_1 = "- hosts: webservers\n\troles:\n\t\t- common\n\t\t- role: foo_app_instance\n\t\t- role: " \
             "foo_app_instance\n- hosts: localhost\n\troles:\n\t\t- common\n\t\t- role: another_instance "
script_0_2 = '---\n-\n- name: "wait for {{ cluster }}.client.admin.keyring exists"\n\twait_for:\n\t\tpath: ' \
             '/etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx\n '
script_6 = "- hosts: webservers\n\tvars:\n\t\t- var_name: not_a_role_var\n\troles:\n\t\t- common\n\t\t- role: " \
           "foo_app_instance\n\t\t\tvars:\n\t\t\t\t dir: '/opt/a'\n\t\t- role: foo_app_instance\n\t\t\tvars: " \
           "\n\t\t\t\t dir: '/opt/b'\n\t\t\t\t app_port: 5000\n- hosts: localhost\n\tvars:\n\t\t- var_name: " \
           "also_not_a_role_var\n\troles:\n\t\t- common\n\t\t- role: another_instance\n\t\t\tvars:\n\t\t\t\tdir: " \
           "'/opt/x' "
script_7 = "- hosts: webservers\n\tvars:\n\t\t- var_name: not_a_role_var\n\troles:\n\t\t- common\n\t\t- role: " \
           "foo_app_instance\n\t\t\tvars:\n\t\t\t\t dir: '/opt/a'\n\t\t- role: foo_app_instance\n\t\t\tvars: " \
           "\n\t\t\t\t dir: '/opt/b'\n\t\t\t\t app_port: 5000\n\n- hosts: localhost\n\tvars:\n\t\t- var_name: " \
           "also_not_a_role_var\n\troles:\n\t\t- common\n\t\t- role: another_instance\n\t\t\tvars:\n\t\t\t\tdir: " \
           "'/opt/x'\n\ttasks:\n\t- shell: /usr/bin/foo\n\t\tregister: foo_result "

TEST_DATA = [
    (script_vars_null, 0),
    (script_0_1, 0),
    (script_0_2, 0),
    (script_6, 6),
    (script_7, 7)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumVars(script).count() == expected
