import pytest
from ansiblemetrics.playbook.num_fact_modules import NumFactModules

script_0_1 = '- name: PRINT START\n\tdebug:\n\t\tmsg: \'I am startinig\'\n- name: PRINT WORKING\n\tdebug:\n\t\tmsg: ' \
             '\'I am working\'\n- name: PRINT END\n\tdebug:\n\t\tmsg: \'I have finished\' '
script_0_2 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not ' \
             'instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring ' \
             'exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx '
script_2 = '- name: Find all instances in the specified region\n\tali_instance_facts:\n\t\talicloud_access_key: \'{{ ' \
           'alicloud_access_key }}\'\n\t\talicloud_secret_key: \'{{ alicloud_secret_key }}\'\n\t\talicloud_region: ' \
           '\'{{ alicloud_region }}\'\n\tregister: all_instances\n\n- name: Find all instances based on the specified ' \
           'ids\n\tali_instance_facts:\n\t\talicloud_access_key: \'{{ alicloud_access_key ' \
           '}}\'\n\t\talicloud_secret_key: \'{{ alicloud_secret_key }}\'\n\t\talicloud_region: \'{{ alicloud_region ' \
           '}}\'\n\tregister: instances_by_ids\n- name: PRINT DATA TO TERMINAL WINDOW\n\tdebug:\n\t\tmsg: \'End of ' \
           'tasks\' '
script_3 = '- name: Find all instances in the specified region\n\tali_instance_facts:\n\t\talicloud_access_key: \'{{ ' \
           'alicloud_access_key }}\'\n\t\talicloud_secret_key: \'{{ alicloud_secret_key }}\'\n\t\talicloud_region: ' \
           '\'{{ alicloud_region }}\'\n\tregister: all_instances\n- name: Find all instances based on the specified ' \
           'ids\n\tali_instance_facts:\n\t\talicloud_access_key: \'{{ alicloud_access_key ' \
           '}}\'\n\t\talicloud_secret_key: \'{{ alicloud_secret_key }}\'\n\t\talicloud_region: \'{{ alicloud_region ' \
           '}}\'\n\tregister: instances_by_ids\n- name: Find all instances based on the specified ' \
           'names/name-prefixes\n\tali_instance_facts:\n\t\talicloud_access_key: \'{{ alicloud_access_key ' \
           '}}\'\n\t\talicloud_secret_key: \'{{ alicloud_secret_key }}\'\n\t\talicloud_region: \'{{ alicloud_region ' \
           '}}\'\n\tregister: instances_by_ids '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_2, 2),
    (script_3, 3)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumFactModules(script).count() == expected
