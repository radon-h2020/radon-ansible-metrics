import re

from ansiblemetrics.utils import keyValueList
from ansiblemetrics.ansible_metric import AnsibleMetric

OPERANDS = r'\{\{\s*[0-9]+\s*(\+|-|\/\/|\/|%|\*\*|\*)\s*[0-9]+\s*\}\}'

class NMO(AnsibleMetric):

    def count(self, relative=False):
        return 0