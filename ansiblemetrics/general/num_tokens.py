import re

import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumTokens(AnsibleMetric):
    """ This class implements the metric 'Number of Tokens' in an Ansible script. """

    def count(self):
        """ Counts the number of tokens in an Ansible script """
        keys = len(utils.all_keys(self.playbook))
        values = utils.all_values(self.playbook)
        return keys + sum(len(re.split(r'\s+', str(value).strip())) for value in values)
