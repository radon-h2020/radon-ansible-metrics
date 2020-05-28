from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.ansible_modules import FILE_MODULES


class NumFileMode(AnsibleMetric):
    """ This class implements the metric 'Number of file mode occurrences' in an Ansible script. """

    def count(self):
        """ Count the number of 'mode' occurrences in a playbook. """

        n_mode = 0

        for task in self.tasks:
            if not task or type(task) != dict:
                continue

            for k, v in task.items():
                if not k or not v:
                    continue

                if k in FILE_MODULES and 'mode' in v:
                    n_mode += 1

        return n_mode
