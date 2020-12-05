import pytest
from ansiblemetrics.playbook.num_uri import NumUri

script_0_1 = '---\n-host: localhost'
script_0_2 = '- oasis_roles.rhsm\n- oasis_roles.molecule_openstack_ci\n- oasis_roles.molecule_docker_ci'
script_1 = '- name: Check that you can connect (GET) to a page and it returns a status 200\n\turi:\n\t\turl: ' \
           'http://www.example.com '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_1, 1)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumUri(script).count() == expected
