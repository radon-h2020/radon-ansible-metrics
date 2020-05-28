import re

from ansiblemetrics.ansible_metric import AnsibleMetric


class NumFileExists(AnsibleMetric):
    """ This class implements the metric 'Number of file exists (exists, islink etc.)' in an Ansible script. """

    # TODO: replace with a more representative name, es Files Check
    def count(self):
        """ Count the number of checks to file existance in a playbook. """

        n_checks = 0

        for task in self.tasks:
            if not task or type(task) != dict:
                continue

            for k, v in task.items():
                if not k or not v:
                    continue

                if k == 'when' and re.match(r'\w+\.(win_)?stat\.\w+\s+is\s*(not)?\s*defined', str(v)):
                    n_checks += 1

        return n_checks
