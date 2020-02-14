import re

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import keyValueList

class NNNV(AnsibleMetric):

    def count(self, relative=False):
        return 0