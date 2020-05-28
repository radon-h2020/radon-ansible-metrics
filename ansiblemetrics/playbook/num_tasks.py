from ansiblemetrics.ansible_metric import AnsibleMetric


class NumTasks(AnsibleMetric):
    """ This class implements the metric 'Number Of Tasks' in an Ansible script. """

    def count(self):
        """ Return the number of tasks in a playbook. """
        return len(self.tasks)
