import pytest
from io import StringIO
from ansiblemetrics.playbook.num_paths import NumPaths

#script_paths
script_0_1 = '---\n-\n\tmartin:\n\t\tjob: Developer\n\t\tname: "Martin Devloper"\n\t\tskills:\n\t\t\t- python\n\t\t\t- perl\n\t\t\t- pascal\n-\n\ttabitha:\n\t\tjob: Developer\n\t\tname: "Tabitha Bitumen"\n\t\tskills:\n\t\t\t- lisp\n\t\t\t- fortran\n\t\t\t- erlang\n'
script_0_2 = '---\n- name: Validate IPMI and instackenv.json\n\thosts: undercloud\n\tgather_facts: yes\n\troles:\n\t\t- validate-ipmi'
script_0_3 = '- oasis_roles.rhsm\n- oasis_roles.molecule_openstack_ci\n- oasis_roles.molecule_docker_ci'
script_3 = '- name: "Downloading {{program_var.stdout}} from Google Drive"\n\tsynchronize:\n\t\tsrc: "/mnt/gdrive/plexguide/backup/{{program_var.stdout}.tar" # 1st path\n\t\tdest: "/tmp"\t# 2nd path\n\tbecome: true\n\tbecome_user: 1000\n\n- name: Remove Password\n\tlineinfile:\n\t\tpath: "/opt/appdata/nzbget/nzbget.conf" # 3rd path\n\t\tregexp: ControlPassword=tegbzn6789\n\t\tline: \'ControlPassword=\'\n\t\tstate: present\n\twhen: nzbget_conf.stat.exists == False' 


TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_0_3, 0),
    (script_3, 3)
]

@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = NumPaths(script).count()
    script.close()
    assert count == expected