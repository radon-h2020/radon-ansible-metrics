import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric

class NINC(AnsibleMetric):

    def count(self, relative=False):
        return 0