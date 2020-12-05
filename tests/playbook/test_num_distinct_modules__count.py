import pytest
from ansiblemetrics.playbook.num_distinct_modules import NumDistinctModules

script_0 = '- name: install httpd and memcached\n\tcustommodule1:\n\t\tname: "{{ item }}"\n\t\tstate: present\n- ' \
           'name: apply the foo config template\n\ttcustommodule3:\n\t\tsrc: templates/src.j2\n\t\tdest: ' \
           '/etc/foo.conf\n- name: start service bar and enable it\n\tcustommodule2:\n\t\tname: bar\n\t\tstate: ' \
           'started '
script_1 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
           'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
           'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_3 = '- name: install httpd and memcached\n\tyum:\n\t\tname: "{{ item }}"\n\t\tstate: present\n- name: apply ' \
           'the foo config template\n\ttemplate:\n\t\tsrc: templates/src.j2\n\t\tdest: /etc/foo.conf\n- name: start ' \
           'service bar and enable it\n\tservice:\n\t\tname: bar\n\t\tstate: started '

TEST_DATA = [
    (script_0, 0),
    (script_1, 1),
    (script_3, 3)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumDistinctModules(script).count() == expected
