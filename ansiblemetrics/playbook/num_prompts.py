from ansiblemetrics.utils import key_value_list

from ansiblemetrics.ansible_metric import AnsibleMetric


class NumPrompts(AnsibleMetric):
    """ This class implements the metric 'Number Of Interactions with User' in an Ansible script. """

    def count(self):
        """ Return the number of prompts in a playbook. """
        return sum(1 for k, v in key_value_list(self.playbook) if k == 'prompt')
