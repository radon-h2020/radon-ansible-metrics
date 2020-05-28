import re

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import key_value_list


class NumNameWithVars(AnsibleMetric):
    """ This class implements the metric 'Number Of Names With Varable' in an Ansible script. """

    def count(self, relative=False):
        """
        Counts the number of names using variables in the script.
        relative: boolean - if True returns the relative number, in the interval [0-1], of names using variables in the script. Default is False.
        """
        names_with_vars = 0

        for k, v in key_value_list(self.playbook):
            if 'name' == k:
                if re.search(r'\{{2,2}\s*([\w\W]+)\s*\}{2,2}', str(v)) is not None:
                    names_with_vars += 1

        return names_with_vars
