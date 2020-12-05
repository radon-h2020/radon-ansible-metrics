import pytest
from ansiblemetrics.playbook.num_regex import NumRegex

script_0_1= '---\n-\n\tmartin:\n\t\tjob: Developer\n\t\tname: "Martin Devloper"\n\t\tskills:\n\t\t\t- python\n\t\t\t- ' \
            'perl\n\t\t\t- pascal\n-\n\ttabitha:\n\t\tjob: Developer\n\t\tname: "Tabitha ' \
            'Bitumen"\n\t\tskills:\n\t\t\t- lisp\n\t\t\t- fortran\n\t\t\t- erlang\n '
script_0_2 = "- oasis_roles.rhsm\n- oasis_roles.molecule_openstack_ci\n- oasis_roles.molecule_docker_ci"
script_1 = '- name: Remove Password\n\tlineinfile:\n\t\tpath: "/opt/appdata/nzbget/nzbget.conf" # 3rd ' \
           'path\n\t\tregexp: ControlPassword=tegbzn6789\n\t\tline: \'ControlPassword=\'\n\t\tstate: present\n\twhen: ' \
           'nzbget_conf.stat.exists == False'

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_1, 1)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumRegex(script).count() == expected
