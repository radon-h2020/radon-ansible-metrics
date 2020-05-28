import pytest
from io import StringIO
from ansiblemetrics.playbook.num_parameters import NumParameters

#script_authorized_key
script_0_1 = '---\n-host: localhost'
script_0_2 = '- oasis_roles.rhsm\n- oasis_roles.molecule_openstack_ci\n- oasis_roles.molecule_docker_ci'
script_3 = '- name: Create two hard links\n\tfile:\n\t\tsrc: \'/tmp/{{ item.src }}\'\n\t\tdest: \'{{ item.dest }}\'\n\t\tstate: hard\n\tloop:\n\t\t- { src: x, dest: y }\n\t\t- { src: z, dest: k }'

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_3, 3)
]

@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = NumParameters(script).count()
    script.close()
    assert count == expected