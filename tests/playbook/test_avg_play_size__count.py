import pytest
from io import StringIO
from ansiblemetrics.playbook.avg_play_size import AveragePlaySize

#script_avgsize
script_0_1 = 'tasks:\n\n- name: GRAB HUE LIGHT INFORMATION\n\turi:\n\t\turl: "http://{{ip_address}}/api/{{username}}"\n\t\tmethod: GET\n\t\tbody: \'{{body_info|to_json}}\'\n\tregister: light_info\n\n'
script_0_2 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx'
script_3 = '---\n- hosts: all\n\troles:\n\t- common\n\n- hosts: dbservers\n\troles:\n\t- db\n\n- hosts: webservers\n\troles:\n\t- base-apache\n\t- web\n\n- hosts: lbservers\n\troles:\n\t- haproxy\n\n- hosts: monitoring\n\troles:\n\t- base-apache\n\t nagios' 

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_3, 3)
]

@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = AveragePlaySize(script).count()
    script.close()
    assert count == expected