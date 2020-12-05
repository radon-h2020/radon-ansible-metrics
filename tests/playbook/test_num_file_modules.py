import pytest
from ansiblemetrics.playbook.num_file_modules import NumFileModules

script_0_1 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_0_2 = '- oasis_roles.rhsm\n- oasis_roles.molecule_openstack_ci\n- oasis_roles.molecule_docker_ci'
script_2 = '- name: Change file ownership, group and permissions\n\tfile:\n\t\tpath: /etc/foo.conf\n\t\towner: ' \
           'foo\n\t\tgroup: foo\n\t\tmode: \'0644\'\n\n- name: Give insecure permissions to an existing ' \
           'file\n\tfile:\n\t\tpath: /work\n\t\towner: root\n\t\tgroup: root\n\t\tmode: \'1777\' '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    count = NumFileModules(script).count()
    assert count == expected
