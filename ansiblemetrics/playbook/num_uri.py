from ansiblemetrics.ansible_metric import AnsibleMetric


class NumUri(AnsibleMetric):
    """ This class implements the metric 'Number of uri' in an Ansible script. """

    def count(self):
        """ Return the number of 'uri' modules in a playbook. """
        return sum(1 for task in self.tasks if task and 'uri' in task)
