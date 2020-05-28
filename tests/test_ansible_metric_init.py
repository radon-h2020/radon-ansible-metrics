import unittest
from io import StringIO
from ansiblemetrics.ansible_metric import AnsibleMetric


class TestAnsibleMetricInit(unittest.TestCase):

    @classmethod
    def __createStream(cls, content):
        return StringIO(content.expandtabs(2))

    @classmethod
    def setUpClass(cls):
        cls.emptyYmlStream = cls.__createStream('')
        cls.invalidYmlStream = cls.__createStream('-\nHello world')

    @classmethod
    def tearDownClass(cls):
        cls.emptyYmlStream.close()
        cls.invalidYmlStream.close()

    def testNone(self):
        with self.assertRaises(TypeError):
            AnsibleMetric(None)

    def testNotStringIO(self):
        with self.assertRaises(TypeError):
            AnsibleMetric('Not a stream io!')

    def testNotPlaybookError1(self):
        with self.assertRaises(TypeError):
            AnsibleMetric(self.invalidYmlStream)

    def testNotPlaybookError2(self):
        with self.assertRaises(TypeError):
            AnsibleMetric(self.emptyYmlStream)

    def testValid1(self):
        script = """# Standards: 0.11\n---\n\n# 3.1.2 Ensure packet redirect sending is disabled\n\n- name: 3.1.2 - Ensure packet redirect sending is disabled\n\tsysctl:\n\t\tignoreerrors: true\n\t\tname: "{{ item }}" \n\t\tvalue: 0\n\t\tstate: present\n\twith_items:\n\t\t- "net.ipv4.conf.all.send_redirects"\n\t\t- "net.ipv4.conf.default.send_redirects"\n\ttags:\n\t\t- level-1\n\t\t- section-3\n\t\t- "3.1.2"\n\t\t- scored\n\n- name: 3.1.2 - Ensure packet redirect sending is disabled in active kernel parameters\n\tcommand: "{{ item }}"\n\twith_items:\n\t\t- "sysctl -w net.ipv4.conf.all.send_redirects=0"\n\t\t- "sysctl -w net.ipv4.conf.default.send_redirects=0"\n\t\t- "sysctl -w net.ipv4.route.flush=1"\n\ttags:\n\t\t- level-1\n\t\t- section-3\n\t\t- "3.1.2"\n\t\t- scored"""
        AnsibleMetric(StringIO(script.expandtabs(2)))


if __name__ == "__main__":
    unittest.main()