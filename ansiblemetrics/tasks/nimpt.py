import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric

class NIMPT(AnsibleMetric):

    def count(self, relative=False):
        return 0