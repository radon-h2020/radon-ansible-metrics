from collections import Counter
from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import keyValueList

class NUN(AnsibleMetric):

    def count(self, relative=False):
        return 0