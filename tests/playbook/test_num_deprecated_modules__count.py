import pytest
from ansiblemetrics.playbook.num_deprecated_modules import NumDeprecatedModules

script_0_1 = '- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML\n\tinclude_vars:\n\t\tfile: username_info.yml\n'
script_0_2 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_2_1 = '- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML\n\tinclude_vars:\n\t\tfile: username_info.yml\n\n- ' \
             'name: Delete a service\n\toc:\n\t\tstate: absent\n\t\tname: myservice\n\t\tnamespace: ' \
             'mynamespace\n\t\tkind: Service\n\n- name: "Access IP Pool 1/3"\n\taos_ip_pool:\n\t\tsession: "{{ ' \
             'aos_session }}"\n\t\tname: "my-ip-pool"\n\t\tsubnets: [ 172.10.0.0/16, 172.12.0.0/16 ]\n\t\tstate: ' \
             'present'
script_2_2 = '- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML\n\tinclude_vars:\n\t\tfile: username_info.yml\n\n- ' \
             'name: Delete a service\n\toc:\n\t\tstate: absent\n\t\tname: myservice\n\t\tnamespace: ' \
             'mynamespace\n\t\tkind: Service\n- name: Delete a service\n\toc:\n\t\tstate: absent\n\t\tname: ' \
             'myservice\n\t\tnamespace: mynamespace\n\t\tkind: Service\n '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_2_1, 2),
    (script_2_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumDeprecatedModules(script).count() == expected
