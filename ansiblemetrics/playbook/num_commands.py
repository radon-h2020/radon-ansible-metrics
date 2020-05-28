from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.ansible_modules import COMMANDS_MODULES


class NumCommands(AnsibleMetric):
    """ This class implements the metric 'Number Of Commands' in an Ansible script. """

    def count(self):
        """ Return the number of 'commands' in a script. """

        commands = 0

        for task in self.tasks:
            if not task or type(task) != dict:
                continue

            if any(key in COMMANDS_MODULES for key in task.keys()):
                commands += 1

        return commands
