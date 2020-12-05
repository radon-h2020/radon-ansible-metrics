import pytest
from ansiblemetrics.playbook.num_external_modules import NumExternalModules

script_0_1 = '- name: PRINT START\n\tdebug:\n\t\tmsg: \'I am startinig\'\n- name: PRINT WORKING\n\tdebug:\n\t\tmsg: ' \
             '\'I am working\'\n- name: PRINT END\n\tdebug:\n\t\tmsg: \'I have finished\' '
script_0_2 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_1 = '- name: ensure foo\n\tfile:\n\t\tpath: /tmp/foo\n\t\tstate: touch\n- name: do a remote ' \
           'copy\n\tremote_copy:\n\t\tsource: /tmp/foo\n\t\tdest: /tmp/bar '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_1, 1)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumExternalModules(script).count() == expected
