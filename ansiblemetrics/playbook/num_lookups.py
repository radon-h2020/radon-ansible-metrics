import re

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import key_value_list


class NumLookups(AnsibleMetric):
    """ This class implements the metric 'Number Of Lookups' in an Ansible script. """

    def count(self):
        """ Return the number of lookups"""
        lookups = 0

        for item in key_value_list(self.playbook):
            v = item[1]
            if re.search(r'\{\{\s*lookup\(.*\)\s*\}\}', str(v)) is not None:
                lookups += 1

        return lookups
