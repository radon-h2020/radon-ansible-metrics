import unittest
from ansiblemetrics.ansible_metric import AnsibleMetric


class TestAnsibleMetricInit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.emptyYmlStream = ''
        cls.invalidYmlStream = '-\nHello world'

    def testNone(self):
        with self.assertRaises(TypeError):
            AnsibleMetric(script=None)

    def testNotPlaybookError1(self):
        with self.assertRaises(TypeError):
            AnsibleMetric(self.invalidYmlStream)

    def testNotPlaybookError2(self):
        with self.assertRaises(TypeError):
            AnsibleMetric(self.emptyYmlStream)

    def testValid1(self):
        script = """# Standards: 0.11\n---\n\n# 3.1.2 Ensure packet redirect sending is disabled\n\n- name: 3.1.2 - 
        Ensure packet redirect sending is disabled\n\tsysctl:\n\t\tignoreerrors: true\n\t\tname: "{{ item }}" 
        \n\t\tvalue: 0\n\t\tstate: present\n\twith_items:\n\t\t- "net.ipv4.conf.all.send_redirects"\n\t\t- 
        "net.ipv4.conf.default.send_redirects"\n\ttags:\n\t\t- level-1\n\t\t- section-3\n\t\t- "3.1.2"\n\t\t- 
        scored\n\n- name: 3.1.2 - Ensure packet redirect sending is disabled in active kernel parameters\n\tcommand: 
        "{{ item }}"\n\twith_items:\n\t\t- "sysctl -w net.ipv4.conf.all.send_redirects=0"\n\t\t- "sysctl -w 
        net.ipv4.conf.default.send_redirects=0"\n\t\t- "sysctl -w net.ipv4.route.flush=1"\n\ttags:\n\t\t- 
        level-1\n\t\t- section-3\n\t\t- "3.1.2"\n\t\t- scored """
        AnsibleMetric(script.expandtabs(2))
