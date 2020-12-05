import pytest
from ansiblemetrics.playbook.avg_task_size import AvgTaskSize

script_0_1 = '- hosts: this is a playbook without tasks\n\tvars:\n\t\thttp_port: 80\n\tremote_user: root'
script_0_2 = '- name: a playbook without tasks\n\thosts: webserver\n\tvars:\n\t\thttp_port: 80\n\tremote_user: root'
script_4_1 = '- name: GRAB HUE LIGHT INFORMATION\n\turi:\n\t\turl: "http://{{ip_address}}/api/{{' \
             'username}}"\n\t\tmethod: GET\n\t\tbody: \'{{body_info|to_json}}\'\n\tregister: light_info\n\n- name: ' \
             'PRINT MESSAGE TO TERMINAL WINDOW\n\tdebug:\n\t\tmsg: "Hello World!"'
script_4_2 = '- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML\n\tinclude_vars:\n\t\tfile: username_info.yml\n\n- ' \
             'name: GRAB HUE LIGHT INFORMATION\n\turi:\n\t\turl: "http://{{ip_address}}/api/{{' \
             'username}}"\n\t\tmethod: GET\n\t\tbody: \'{{body_info|to_json}}\'\n\tregister: light_info\n\n- name: ' \
             'PRINT DATA TO TERMINAL WINDOW\n\tdebug:\n\t\tvar: light_info.json.lights '
script_4_3 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_4_4 = '- hosts: webservers\n\tvars:\n\t\thttp_port: 80\n\tremote_user: root\n\n\ttasks:\n\t- name: ensure ' \
             'apache is at the latest version\n\t\tyum:\n\t\t\tname: httpd\n\t\t\tstate: latest\n\n- hosts: ' \
             'databases\t\n\tremote_user: root\n\n\ttasks:\n\t- name: ensure postgresql is at the latest ' \
             'version\n\t\tyum:\n\t\t\tname: postgresql\n\t\t\tstate: latest\n\t\t\n\t- name: ensure that postgresql ' \
             'is started\n\t\tservice:\n\t\t\tname: postgresql\n\t\t\tstate: started\n '


TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_4_1, 4),
    (script_4_2, 4),
    (script_4_3, 4),
    (script_4_4, 4)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert AvgTaskSize(script).count() == expected
