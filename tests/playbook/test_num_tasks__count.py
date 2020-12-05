import pytest
from ansiblemetrics.playbook.num_tasks import NumTasks

script_1 = '- hosts: this is a playbook\n\ttasks:\n\t\t-name: FIRST TASK'
script_4 = '- name: ensure apache is at the latest version\n\tyum: name=httpd state=latest\n- name: write the apache ' \
           'config file\n\ttemplate: src=/srv/httpd.j2 dest=/etc/httpd.conf\n- name: ensure postgresql is at the ' \
           'latest version\n\tyum: name=postgresql state=latest\n- name: ensure that postgresql is ' \
           'started\n\tservice: name=postgresql state=started\n '

TEST_DATA = [
    (script_1, 1),
    (script_4, 4)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumTasks(script).count() == expected
