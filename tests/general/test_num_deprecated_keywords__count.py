import pytest
from ansiblemetrics.general.num_deprecated_keywords import NumDeprecatedKeywords

script_0 = '- hosts: localhost\n\ttasks:\n\n\t- name: Hello, Ansible!\n\t\taction: rust_helloworld'
script_2 = 'tasks:\n\n- name: Hello, Ansible!\n\taction: rust_helloworld\n\targs:\n\t\tname: Ansible\n\tregister: ' \
           'hello_ansible\n\n- name: Async Hello, World!\n\taction: rust_helloworld\n\tasync: 10\n\tpoll: ' \
           '1\n\tregister: async_hello_world\n\n- name: Async Hello, Ansible!\n\taction: ' \
           'rust_helloworld\n\targs:\n\t\tname: Ansible\n\tasync: 10\n\tpoll: 1\n\tregister: async_hello_ansible '

TEST_DATA = [
    (script_0, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumDeprecatedKeywords(script).count() == expected
