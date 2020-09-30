import yaml
from io import StringIO

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.general.lines_code import LinesCode


class AvgTaskSize(AnsibleMetric):
    """ This class implements the metric 'Average Task Size' in an Ansible script. """

    def count(self):
        """ Return the average size of the tasks. """

        size = 0
        n_tasks = 0
        for task in self.tasks:
            if not task:
                continue

            n_tasks += 1
            size += LinesCode(StringIO(yaml.dump(task))).count()

        return int(round(size / n_tasks)) if n_tasks else 0
