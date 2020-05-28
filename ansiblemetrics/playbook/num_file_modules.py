from ansiblemetrics.ansible_metric import AnsibleMetric

class NumFileModules(AnsibleMetric):
    """ This class implements the metric 'Number Of file Modules' in an Ansible script. """

    def count(self):
        """ Count the number of 'file' occurrences in a playbook. """
        return sum(1 for task in self.tasks if task and 'file' in task)