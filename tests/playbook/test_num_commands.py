import pytest
from ansiblemetrics.playbook.num_commands import NumCommands

script_0_1 = '---\n-\n\tmartin:\n\t\tjob: Developer\n\t\tname: "Martin Devloper"\n\t\tskills:\n\t\t\t- ' \
             'python\n\t\t\t- perl\n\t\t\t- pascal\n-\n\ttabitha:\n\t\tjob: Developer\n\t\tname: "Tabitha ' \
             'Bitumen"\n\t\tskills:\n\t\t\t- lisp\n\t\t\t- fortran\n\t\t\t- erlang\n '
script_0_2 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_0_3 = '- oasis_roles.rhsm\n- oasis_roles.molecule_openstack_ci\n- oasis_roles.molecule_docker_ci'
script_8 = '- name: return motd to registered var\n\tcommand: cat /etc/motd\n\tregister: mymotd\n\n- name: Case ' \
           'insensitive password string match\n\texpect:\n\t\tcommand: passwd username\n\t\tresponses:\n\t\t\t(' \
           '?i)password: "MySekretPa$$word"\n\tno_log: true\n\n- name: Run a cmd.exe ' \
           'command\n\tpsexec:\n\t\thostname: server\n\t\tconnection_username: username\n\t\tconnection_password: ' \
           'password\n\t\texecutable: cmd.exe\n\t\targuments: /c echo Hello World\n\n- name: List user accounts on a ' \
           'Windows system\n\traw: Get-WmiObject -Class Win32_UserAccount\n\n- name: Run a script with arguments (' \
           'free form)\n\tscript: /some/local/script.sh --some-argument 1234\n\n- name: Execute the command in remote ' \
           'shell; stdout goes to the specified file on the remote.\n\tshell: somescript.sh >> somelog.txt\n\n- name: ' \
           'Change the working directory to somedir/ before executing the command.\n\tshell: somescript.sh >> ' \
           'somelog.txt\n\targs:\n\t\tchdir: somedir/\n\n- name: run show commands\n\ttelnet:\n\t\tuser: ' \
           'cisco\n\t\tpassword: cisco\n\t\tlogin_prompt: "Username: "\n\t\tprompts:\n\t\t\t- "[' \
           '>#]"\n\t\tcommand:\n\t\t\t- terminal length 0\n\t\t\t- show version '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_0_3, 0),
    (script_8, 8)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumCommands(script).count() == expected
