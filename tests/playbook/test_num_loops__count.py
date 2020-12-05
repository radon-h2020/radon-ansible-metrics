import pytest
from ansiblemetrics.playbook.num_loops import NumLoops

script_0 = '- name: add several users\n\tuser:\n\t\tname: "{{ item }}"\n\t\tstate: present\n\t\tgroups: "wheel"\n'
script_1 = '---\n- name: Ensure Datadog repository is up-to-date\n\tapt_repository:\n\tfilename: ' \
           'ansible_datadog_agent\n\trepo: "{{ item.value }}"\n\tstate: "{% if item.key == ' \
           'datadog_agent_major_version|int and datadog_apt_repo | length == 0 %}present{% else %}absent{% endif ' \
           '%}"\n\tupdate_cache: yes\n\twhen: (not ansible_check_mode)\n\twith_dict:\n\t5: "{{ ' \
           'datadog_agent5_apt_repo }}"\n\t6: "{{ datadog_agent6_apt_repo }}"\n\t7: "{{ datadog_agent7_apt_repo }}"\n '
script_2 = '- name: with_list\n\tdebug:\n\t\tmsg: "{{ item }}"\n\twith_list:\n\t\t- one\n\t\t- two\n\n- name: ' \
           'with_list -> loop\n\tdebug:\n\t\tmsg: "{{ item }}"\n\tloop:\n\t\t- one '

TEST_DATA = [
    (script_0, 0),
    (script_1, 1),
    (script_2, 2)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumLoops(script).count() == expected
