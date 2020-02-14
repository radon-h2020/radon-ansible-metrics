import re

from ansiblemetrics.utils import keyValueList
from ansiblemetrics.ansible_metric import AnsibleMetric

regex = re.compile(r'\band\b | \bor\b | \bnot\b', flags=re.X)

class NLO(AnsibleMetric):

    def count(self, relative=False):
        return 0