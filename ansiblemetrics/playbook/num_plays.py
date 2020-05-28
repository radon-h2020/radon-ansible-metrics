from ansiblemetrics.ansible_metric import AnsibleMetric


class NumPlays(AnsibleMetric):
    """ This class implements the metric 'Number Of Plays' in an Ansible script. """

    def count(self):
        """ Return the number of plays in a playbook. """
        return len(self.plays)
