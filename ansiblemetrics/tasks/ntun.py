from collections import Counter
from ansiblemetrics.ansible_metric import AnsibleMetric

class NTUN(AnsibleMetric):

    def count(self, relative=False):
        return 0