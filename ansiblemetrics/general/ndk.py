import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_keywords import DEPRECATED_KEYWORDS
from ansiblemetrics.ansible_metric import AnsibleMetric

class NDK(AnsibleMetric):

    def count(self, relative=False):
        return 0