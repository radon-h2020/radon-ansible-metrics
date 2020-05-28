import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumLoops(AnsibleMetric):
    """ This class implements the metric 'Number of standard loops' in an Ansible script. """

    def count(self):
        """ Return the number of standard loops. """
        return sum(1 for key in utils.all_keys(self.playbook) if key == 'loop' or str(key).startswith('with_'))
