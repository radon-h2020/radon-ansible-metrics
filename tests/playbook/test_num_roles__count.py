import pytest
from ansiblemetrics.playbook.num_roles import NumRoles

script_0_1 = '---\n-\n\tmartin:\n\t\tjob: Developer\n\t\tname: "Martin Devloper"\n\t\tskills:\n\t\t\t- ' \
             'python\n\t\t\t- perl\n\t\t\t- pascal\n-\n\ttabitha:\n\t\tjob: Developer\n\t\tname: "Tabitha ' \
             'Bitumen"\n\t\tskills:\n\t\t\t- lisp\n\t\t\t- fortran\n\t\t\t- erlang\n '
script_0_2 = '---\n-\n- name: "wait for {{ cluster }}.client.admin.keyring exists"\n\twait_for:\n\t\tpath: ' \
             '/etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx\n '
script_1 = '- hosts: all\n\tname: Given no previous deploy with SVN\n\ttasks:\n\t- name: Assert ansistrano_deploy_to ' \
           'path does not exist\n\t\tregister: st\n\t\tstat:\n\t\t\tpath: \'{{ ansistrano_deploy_to }}\'\n\t- ' \
           'debug:\n\t\t\tmsg: Path does not exist and is a directory\n\t\twhen: st.stat.exists is defined and not ' \
           'st.stat.exists\n\tvars:\n\t\tansistrano_deploy_to: /tmp/svn/my-app.com\n- hosts: all\n\tname: When ' \
           'deploying using SVN\n\troles:\n\t- role: local-ansistrano\n\tvars:\n\t\tansistrano_deploy_to: ' \
           '/tmp/svn/my-app.com\n\t\tansistrano_deploy_via: svn\n\t\tansistrano_svn_repo: ' \
           'https://github.com/ansistrano/deploy.git\n- hosts: all\n\tname: Then a successful deploy with svn should ' \
           'be done\n\ttasks:\n\t- name: Assert ansistrano_deploy_to path does exist\n\t\tregister: ' \
           'st\n\t\tstat:\n\t\t\tpath: \'{{ ansistrano_deploy_to }}\'\n\t- debug:\n\t\t\tmsg: Path exists and is a ' \
           'directory\n\t\twhen: st.stat.exists is defined and st.stat.exists\n\tvars:\n\t\tansistrano_deploy_to: ' \
           '/tmp/svn/my-app.com\n- hosts: all\n\tname: And I should be able to do a second deploy\n\troles:\n\t- ' \
           'role: local-ansistrano\n\tvars:\n\t\tansistrano_deploy_to: ' \
           '/tmp/svn/my-app.com\n\t\tansistrano_deploy_via: svn\n\t\tansistrano_svn_repo: ' \
           'https://github.com/ansistrano/deploy.git '
script_2 = '- become: true\n\tenvironment: \'{{ inventory__environment | d({}) | combine(' \
           'inventory__group_environment\n\t\t| d({})) | combine(inventory__host_environment\t| d({})) ' \
           '}}\'\n\thosts:\n\t- debops_service_libvirtd_qemu\n\tname: Install and manage libvirtd QEMU ' \
           'configuration\n\troles:\n\t- ferm__dependent_rules:\n\t\t- \'{{ libvirtd_qemu__ferm__dependent_rules ' \
           '}}\'\n\t\trole: debops.ferm\n\t\ttags:\n\t\t- role::ferm\n\t\t- skip::ferm\n\t- role: ' \
           'debops.libvirtd_qemu\n\t\ttags:\n\t\t- role::libvirtd_qemu\n\t\t- skip::libvirtd_qemu '
script_6 = '---\n\n- hosts: all\n\n\troles:\n\t- common\n\n- hosts: dbservers\n\n\troles:\n\t- db\n\n- hosts: ' \
           'webservers\n\n\troles:\n\t- base-apache\n\t- web\n\n- hosts: lbservers\n\n\troles:\n\t- haproxy\n \n- ' \
           'hosts: monitoring\n\n\troles:\n\t- base-apache\n\t- nagios\n '

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_1, 1),
    (script_2, 2),
    (script_6, 6)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    assert NumRoles(script).count() == expected
