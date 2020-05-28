import re

from ansiblemetrics.utils import key_value_list
from ansiblemetrics.ansible_metric import AnsibleMetric

OPERANDS = r'\{\{\s*[0-9]+\s*(\+|-|\/\/|\/|%|\*\*|\*)\s*[0-9]+\s*\}\}'


class NumMathOperations(AnsibleMetric):
    """ This class implements the metric 'Number of maths operations' in an Ansible script. """

    def count(self):
        return sum(len(re.findall(OPERANDS, str(v))) for k, v in key_value_list(self.playbook))
