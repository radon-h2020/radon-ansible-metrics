import re
import yaml
from io import StringIO

from ansiblemetrics.exceptions import NotStringIOError
from ansiblemetrics.ansible_metric import AnsibleMetric

class NSCM(AnsibleMetric):
    
    def count(self, relative=False):
        return 0