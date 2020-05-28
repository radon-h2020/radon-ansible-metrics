from ansiblemetrics.ansible_metric import AnsibleMetric


class NumBlocksErrorHandling(AnsibleMetric):
    """ This class implements the metric 'Number Of Blocks Error Handling' in an Ansible script. """

    def count(self):
        """ Returns the number of number of blocks error handling in tasks. """
        handled = 0

        for task in self.tasks:
            if task and 'block' in task and ('rescue' in task or 'always' in task):
                handled += 1

        return handled
