import pytest
from ansiblemetrics.playbook.num_plays import NumPlays

script_0_1 = '---\n-\n\tmartin:\n\t\tjob: Developer\n\t\tname: "Martin Devloper"\n\t\tskills:\n\t\t\t- ' \
             'python\n\t\t\t- perl\n\t\t\t- pascal\n-\n\ttabitha:\n\t\tjob: Developer\n\t\tname: "Tabitha ' \
             'Bitumen"\n\t\tskills:\n\t\t\t- lisp\n\t\t\t- fortran\n\t\t\t- erlang\n '
script_0_2 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_2 = '---\n- hosts: webservers\n\tremote_user: root\n\n\ttasks:\n\t- name: ensure apache is at the latest ' \
           'version\n\t\tyum: name=httpd state=latest\n\t- name: write the apache config file\n\t\ttemplate: ' \
           'src=/srv/httpd.j2 dest=/etc/httpd.conf\n\n- hosts: databases\n\tremote_user: root\n\n\ttasks:\n\t- name: ' \
           'ensure postgresql is at the latest version\n\t\tyum: name=postgresql state=latest\n\t- name: ensure that ' \
           'postgresql is started\n\t\tservice: name=postgresql state=started\n '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumPlays(script).count() == expected
