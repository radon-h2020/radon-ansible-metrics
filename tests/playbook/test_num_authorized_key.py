import pytest
from ansiblemetrics.playbook.num_authorized_key import NumAuthorizedKey

script_0_1 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_0_2 = '- oasis_roles.rhsm\n- oasis_roles.molecule_openstack_ci\n- oasis_roles.molecule_docker_ci'
script_1 = '- name: Set authorized key taken from file\n\tauthorized_key:\n\t\tuser: charlie\n\t\tstate: ' \
           'present\n\t\tkey: "{{ lookup(\'file\', \'/home/charlie/.ssh/id_rsa.pub\') }}" '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_1, 1)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumAuthorizedKey(script).count() == expected
