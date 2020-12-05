import pytest
from ansiblemetrics.playbook.num_file_exists import NumFileExists

script_0_1 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_0_2 = '- oasis_roles.rhsm\n- oasis_roles.molecule_openstack_ci\n- oasis_roles.molecule_docker_ci'
script_2 = '- debug:\n\t\tmsg: "Path exists and is not a symlink"\n\twhen: sym.stat.exists is defined and ' \
           'sym.stat.exists == False\n\n- stat:\n\t\tpath: /path/to/something\n\tregister: p\n- debug:\n\t\tmsg: ' \
           '"Path exists and is a directory"\n\twhen: p.stat.isdir is defined and p.stat.isdir '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumFileExists(script).count() == expected