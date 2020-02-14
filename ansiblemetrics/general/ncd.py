import re

from ansiblemetrics.utils import keyValueList
from ansiblemetrics.ansible_metric import AnsibleMetric

LOGIC_OPERANDS = re.compile(r'\band\b|\bor\b', flags=re.X)

class NCD(AnsibleMetric):
    """ This class implements the metric 'Number of conditions' in an Ansible script. """

    def count(self):
        return 0