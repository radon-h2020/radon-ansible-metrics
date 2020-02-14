from ansiblemetrics.utils import keyValueList

from ansiblemetrics.ansible_metric import AnsibleMetric

class NIU(AnsibleMetric):

    def count(self, relative=False):
        return 0