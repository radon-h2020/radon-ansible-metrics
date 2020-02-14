from collections import Counter
from ansiblemetrics.ansible_metric import AnsibleMetric

class NPUN(AnsibleMetric):

    def count(self, relative=False):
        return 0