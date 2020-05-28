import pytest
from io import StringIO
from ansiblemetrics.general.num_keys import NumKeys

#script_keys
script_9 = '- hosts: all\n\troles:\n\t- common\n\n- hosts: dbservers\n\troles:\n\t- db\n\n\ttasks: \n\t- name: Create Application Database\n\t\tmysql_db:\n\t\t\tname: "{{ dbname }}"\n\t\t\tstate: present'

TEST_DATA = [
    (script_9, 9)
]

@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = NumKeys(script).count()
    script.close()
    assert count == expected