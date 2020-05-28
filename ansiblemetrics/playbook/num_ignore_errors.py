from ansiblemetrics.ansible_metric import AnsibleMetric


class NumIgnoreErrors(AnsibleMetric):
    """ This class implements the metric 'Number Of ignore_errors' in an Ansible script. """

    def count(self):
        """ Counts the number of ignore_errors"""

        ignore_errors = 0
        for task in self.tasks:
            if not task:
                continue

            if 'ignore_errors' in task and task['ignore_errors'] in ('yes', True):
                ignore_errors += 1

        return ignore_errors
