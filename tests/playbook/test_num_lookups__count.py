import pytest
from ansiblemetrics.playbook.num_lookups import NumLookups

script_0 = '- hosts: all\n\tvars:\n\t\tcontents: "static content"\n\n\ttasks:\n\t\t- debug: msg="the value of foo.txt ' \
           'is {{ contents }}" '
script_1 = '- hosts: all\n\tvars:\n\t\tcontents: "{{ lookup(\'file\', \'/etc/foo.txt\') }}"\n\n\ttasks:\n\t\t- debug: ' \
           'msg="the value of foo.txt is {{ contents }}" '
script_2_1 = '- hosts: all\n\n\ttasks:\n\n\t\t- mysql_user: name={{ client }}\n\t\t\t\t\t\t\t\t\tpassword="{{ lookup(' \
             '\'password\', \'/tmp/passwordfile chars=ascii_letters\') }}"\n\t\t\t\t\t\t\t\t\tpriv={{ client }}_{{ ' \
             'tier }}_{{ role }}.*:ALL\n\n\t\t- mysql_user: name={{ client }}\n\t\t\t\t\t\t\t\t\tpassword="{{ lookup(' \
             '\'password\', \'/tmp/passwordfile chars=digits\') }}"\n\t\t\t\t\t\t\t\t\tpriv={{ client }}_{{ tier }}_{' \
             '{ role }}.*:ALL\n\n\t\t- mysql_user: name={{ client }}\n\t\t\t\t\t\t\t\t\tpriv={{ client }}_{{ tier ' \
             '}}_{{ role }}.*:ALL '
script_2_2 = 'tasks:\n\n\t- mysql_user: name={{ client }}\n\t\t\t\t\t\t\t\tpassword="{{ lookup(\'password\', ' \
             '\'/tmp/passwordfile chars=ascii_letters\') }}"\n\t\t\t\t\t\t\t\tpriv={{ client }}_{{ tier }}_{{ role ' \
             '}}.*:ALL\n\n\t- mysql_user: name={{ client }}\n\t\t\t\t\t\t\t\tpassword="{{ lookup(\'password\', ' \
             '\'/tmp/passwordfile chars=digits\') }}"\n\t\t\t\t\t\t\t\tpriv={{ client }}_{{ tier }}_{{ role ' \
             '}}.*:ALL\n\n\t- mysql_user: name={{ client }}\n\t\t\t\t\t\t\t\tpriv={{ client }}_{{ tier }}_{{ role ' \
             '}}.*:ALL '

TEST_DATA = [
    (script_0, 0),
    (script_1, 1),
    (script_2_1, 2),
    (script_2_1, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumLookups(script).count() == expected
