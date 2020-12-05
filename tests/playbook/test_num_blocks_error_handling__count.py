import pytest
from ansiblemetrics.playbook.num_blocks_error_handling import NumBlocksErrorHandling

script_0_1 = '- name: disable the server in haproxy\n\tshell: echo "disable server myapplb/{{ inventory_hostname }}" ' \
             '| socat stdio /var/lib/haproxy/stats\n\tdelegate_to: "{{ item }}"\n\tloop: "{{ groups.lbservers }}" '
script_0_2 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_1 = '- name: Attempt and graceful roll back demo\n\tblock:\n\t\t- debug:\n\t\t\t\tmsg: \'I execute ' \
           'normally\'\n\t\t- name: i force a failure\n\t\t\tcommand: /bin/false\n\t\t- debug:\n\t\t\t\tmsg: \'I ' \
           'never execute, due to the above task failing, :-(\'\n\trescue:\n\t\t- debug:\n\t\t\t\tmsg: \'I caught an ' \
           'error\'\n\t\t- name: i force a failure in middle of recovery! >:-)\n\t\t\tcommand: /bin/false\n\t\t- ' \
           'debug:\n\t\t\t\tmsg: \'I also never execute :-(\'\n\talways:\n\t\t- debug:\n\t\t\t\tmsg: "This always ' \
           'executes"\n\n- name: A task with a block that does not handle errors\n\tblock:\n\t\t- ' \
           'debug:\n\t\t\t\tmsg: \'I execute normally\'\n\t\t- name: i force a failure\n\t\t\tcommand: ' \
           '/bin/false\n\t\t- debug:\n\t\t\t\tmsg: \'I never execute, due to the above task failing, :-(\' '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_1, 1)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumBlocksErrorHandling(script).count() == expected
