from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import keyValueList
import re

class NTVR(AnsibleMetric):

    def count(self, relative=False):
        return 0