import pytest
from ansiblemetrics.general.num_suspicious_comments import NumSuspiciousComments

script_0 = '- hosts: all\n\troles:\n\t- common\n\n- hosts: dbservers\n\troles:\n\t- db\n\n\ttasks: \n\t- name: Create ' \
           'Application Database\n\t\tmysql_db:\n\t\t\tname: "{{ dbname }}"\n\t\t\tstate: present '
script_2 = '# TODO: Remove this task after Ansible 2.x npm module bug is fixed. See:\n# ' \
           'https://github.com/ansible/ansible-modules-extras/issues/1375\n- name: Ensure forever is installed (to ' \
           'run Node.js apps).\n\tnpm: name=forever global=yes state=present\n\tbecome: yes\n\tbecome_user: "{{ ' \
           'nodejs_install_npm_user }}"\n\twhen: nodejs_forever\n# TODO: Remove this task after Ansible 2.x npm ' \
           'module bug is fixed. See:\n# https://github.com/ansible/ansible-modules-extras/issues/1375\n- name: ' \
           'Ensure forever is at the latest release.\n\tnpm: name=forever global=yes state=latest\n\tbecome: ' \
           'yes\n\tbecome_user: "{{ nodejs_install_npm_user }}"\n\twhen: nodejs_forever '


TEST_DATA = [
    (script_0, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumSuspiciousComments(script).count() == expected
