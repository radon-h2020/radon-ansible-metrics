import pytest
from ansiblemetrics.playbook.num_paths import NumPaths

script_0 = '---\n- name: Validate IPMI and instackenv.json\n\thosts: undercloud\n\tgather_facts: ' \
             'yes\n\troles:\n\t\t- validate-ipmi '
script_3 = '- name: "Downloading {{program_var.stdout}} from Google Drive"\n\tsynchronize:\n\t\tsrc: ' \
           '"/mnt/gdrive/plexguide/backup/{{program_var.stdout}.tar" # 1st path\n\t\tdest: "/tmp"\t# 2nd ' \
           'path\n\tbecome: true\n\tbecome_user: 1000\n\n- name: Remove Password\n\tlineinfile:\n\t\tpath: ' \
           '"/opt/appdata/nzbget/nzbget.conf" # 3rd path\n\t\tregexp: ControlPassword=tegbzn6789\n\t\tline: ' \
           '\'ControlPassword=\'\n\t\tstate: present\n\twhen: nzbget_conf.stat.exists == False'


TEST_DATA = [
    (script_0, 0),
    (script_3, 3)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumPaths(script).count() == expected
