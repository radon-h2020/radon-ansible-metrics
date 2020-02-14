import re

from ansiblemetrics.utils import keyValueList
from ansiblemetrics.ansible_metric import AnsibleMetric

regex = re.compile(r'\bif\b|\belif\b|\belse\b')


class NICD(AnsibleMetric):

    def count(self, relative=False):
        return 0