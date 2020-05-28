import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumKeys(AnsibleMetric):
    """ This class implements the metric 'Number of keys' in an Ansible script. """

    def count(self):
        return len(utils.all_keys(self.playbook))
