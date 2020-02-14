import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric

class NIMPR(AnsibleMetric):

    def count(self, relative=False):
        return 0