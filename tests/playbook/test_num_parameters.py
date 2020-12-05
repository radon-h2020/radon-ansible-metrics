import pytest
from ansiblemetrics.playbook.num_parameters import NumParameters

script_0_1 = '---\n-host: localhost'
script_0_2 = '- oasis_roles.rhsm\n- oasis_roles.molecule_openstack_ci\n- oasis_roles.molecule_docker_ci'
script_3 = '- name: Create two hard links\n\tfile:\n\t\tsrc: \'/tmp/{{ item.src }}\'\n\t\tdest: \'{{ item.dest ' \
           '}}\'\n\t\tstate: hard\n\tloop:\n\t\t- { src: x, dest: y }\n\t\t- { src: z, dest: k } '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_3, 3)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumParameters(script).count() == expected
