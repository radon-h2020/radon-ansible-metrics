from ansiblemetrics.ansible_modules import DEPRECATED_MODULES_LIST
from ansiblemetrics.ansible_metric import AnsibleMetric

class NDM(AnsibleMetric):

    def count(self, relative=False):
        return 0