import pytest
from ansiblemetrics.playbook.num_blocks import NumBlocks

script_0_1 = '- name: This command will change the working directory to somedir/ and will only run when ' \
             'somedir/somelog.txt does not exist.\n\tshell: somescript.sh >> somelog.txt\n\ttargs:\n\t\tchdir: ' \
             'somedir/\n\t\tpcreates: somelog.txt '
script_0_2 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_1 = '- name: Install, configure, and start Apache\n\tblock:\n\t- name: start service bar and enable ' \
           'it\n\t\tservice:\n\t\t\tname: bar\n\t\t\tstate: started\n\t\t\tenabled: True\n\twhen: ansible_facts[' \
           '\'distribution\'] == \'CentOS\' '
script_2 = '- name: Install, configure, and start Apache\n\tblock:\n\t- name: start service bar and enable ' \
           'it\n\t\tservice:\n\t\tname: bar\n\t\tstate: started\n\t\tenabled: True\n\twhen: ansible_facts[' \
           '\'distribution\'] == \'CentOS\'\n\n- name: Attempt and graceful roll back demo\n\tblock:\n\t- ' \
           'debug:\n\t\tmsg: \'I execute normally\'\n\t- name: i force a failure\n\t\tcommand: /bin/false\n\t- ' \
           'debug:\n\t\tmsg: \'I never execute, due to the above task failing, :-(\' '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_1, 1),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumBlocks(script).count() == expected
