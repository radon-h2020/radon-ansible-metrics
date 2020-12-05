import pytest
from ansiblemetrics.general.num_conditions import NumConditions

script_0 = '- hosts: localhost\n\ttasks:\n\n\t- name: Hello, Ansible!\n\t\taction: ' \
           'rust_helloworld\n\t\targs:\n\t\t\tname: Ansible\n\t\tregister: hello_ansible\n\n\t- name: Async Hello, ' \
           'World!\n\t\taction: rust_helloworld\n\t\tasync: 10\n\t\tpoll: 1\n\t\tregister: async_hello_world\n\n\t- ' \
           'name: Async Hello, Ansible!\n\t\taction: rust_helloworld\n\t\targs:\n\t\t\tname: Ansible\n\t\tasync: ' \
           '10\n\t\tpoll: 1\n\t\tregister: async_hello_ansible '
script_1 = '---\n- block:\n\n\t\t- name: COMMAND | Create /usr/local/etc/fdfs/http.conf\n\t\t\tcommand: touch ' \
           '/usr/local/etc/fdfs/http.conf\n\t\t\targs:\n\t\t\t\tcreates: ' \
           '/usr/local/etc/fdfs/http.conf\n\t\t\tregister: fd1\n\n\twhen: true\n '
script_3 = '- name: Prepare PostgreSQL | check PostgreSQL is started\n\tchanged_when: false\n\tfailed_when:\n\t\t- ' \
           'pg_ctl_status_result.rc != 0\n\t\t- pg_ctl_status_result.rc != 3\n '
script_5 = '- hosts: all\n\ttest1: "Hello World"\n\ttasks:\n\t- debug:\n\t\tmsg: "Equals"\n\t\twhen:\n\t\t\t- test1 ' \
           '== "Hello World"\n\t\t\t- test1 != "Hello"\n\t- debug:\n\t\t\tmsg: "Not Equals"\n\t\t\twhen: test1 != ' \
           '"Hello World"\n\t- debug:\n\t\t\tmsg: "Not Equals"\n\t\t\twhen: test1 <= 5 or test1 >= 10 '

TEST_DATA = [
    (script_0, 0),
    (script_1, 1),
    (script_3, 3),
    (script_5, 5)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumConditions(script).count() == expected

