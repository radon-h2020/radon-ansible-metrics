import re
from collections import Counter

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import keyValueList

filter_regex = re.compile(r'[^\|]+(\|)[^\|]')

class NFL(AnsibleMetric):

    def count(self, relative=False):
        return 0