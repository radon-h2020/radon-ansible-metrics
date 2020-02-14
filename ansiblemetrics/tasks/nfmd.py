from ansiblemetrics.ansible_modules import ANSIBLE_MODULES_LIST, FACT_MODULES_LIST
from ansiblemetrics.ansible_metric import AnsibleMetric

class NFMD(AnsibleMetric):

    def count(self, relative=False):
        return 0