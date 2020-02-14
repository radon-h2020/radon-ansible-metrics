from ansiblemetrics.ansible_modules import ANSIBLE_MODULES_LIST
from ansiblemetrics.ansible_keywords import TASK_KEYWORDS
from ansiblemetrics.ansible_metric import AnsibleMetric

class NEMD(AnsibleMetric):

    def count(self, relative=False):
        return 0