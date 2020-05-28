from ansiblemetrics.ansible_metric import AnsibleMetric

class NumAuthorizedKey(AnsibleMetric):
    """ This class implements the metric 'Number of times a SSH key is set andd/or updated' in an Ansible script. """

    def count(self):
        """ Count the number of 'authorized_key' occurrences in a playbook. """
        
        return sum(1 for task in self.playbook if task and 'authorized_key' in task)