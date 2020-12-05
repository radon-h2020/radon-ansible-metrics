import pytest
from ansiblemetrics.general.num_decisions import NumDecisions

script_0_1 = "- hosts: localhost \n\ttasks:\n\t\t- shell: echo \"I've got '{{ foo }}' and am not afraid to use " \
             "it!\"\n\t\t\twhen: foo is defined\n\t\t- fail: msg=\"Bailing out. this play requires 'bar' and 'foo'\"\n "
script_0_2 = '- become: true\n\tgather_facts: true\n\thandlers:\n\t- import_tasks: handlers.yml\n\thosts: ' \
             'drucker_web\n\ttasks:\n\t- import_tasks: plays/drupal/drupal-create.yml\n\tvars_files:\n\t- vars.yml\n '
script_0_3 = '---\n-\n- name: "wait for {{ cluster }}.client.admin.keyring exists"\n\twait_for:\n\t\tpath: ' \
             '/etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx\n '
script_0_4 = '---\n- block:\n\n\t\t- name: COMMAND | Create /usr/local/etc/fdfs/http.conf\n\t\t\tcommand: touch ' \
             '/usr/local/etc/fdfs/http.conf\n\t\t\targs:\n\t\t\t\tcreates: ' \
             '/usr/local/etc/fdfs/http.conf\n\t\t\tregister: fd1\n\n\twhen: true\n '
script_1 = '- name: Prepare PostgreSQL | check PostgreSQL is started\n\tchanged_when: false\n\tfailed_when:\n\t\t- ' \
           'pg_ctl_status_result.rc != 0\n\t\t- pg_ctl_status_result.rc != 3\n '
script_4 = '- hosts: all\n\ttest1: "Hello World"\n\ttest2: "Hello Space"\n\ttasks:\n\t- debug:\n\t\t\tmsg: ' \
           '"Equals"\n\t\t\twhen: test1 == "Hello World" or test1 == "Hello"\n\t- debug:\n\t\t\tmsg: "Not ' \
           'Equals"\n\t\t\twhen: \n\t\t\t\t- test1 == "Hello World" and not test2 == test1\n\t\t\t\t- test3 == "Waldo" '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_0_3, 0),
    (script_0_4, 0),
    (script_1, 1),
    (script_4, 4)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumDecisions(script).count() == expected
