import re

from ansiblemetrics.utils import keyValueList
from ansiblemetrics.ansible_metric import AnsibleMetric

COMPARISON_OPERANDS = re.compile(r'\bis\b|\bin\b|\bnot\b|==|!=|>=|>|<=|<')

class NCO(AnsibleMetric):

    def count(self, relative=False):
        return 0