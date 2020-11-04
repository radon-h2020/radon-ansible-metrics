import yaml
from io import StringIO

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.general.lines_code import LinesCode
from ansiblemetrics.playbook.num_plays import NumPlays


class AveragePlaySize(AnsibleMetric):
    """ This class implements the metric 'Average Play Size' in an Ansible script. """

    def count(self):
        """ Return the average size of plays in a playbook in terms of lines of code, 0 if the file contains no plays."""
        plainYaml = StringIO(yaml.dump(self.playbook))
        loc = LinesCode(plainYaml).count()
        plays = NumPlays(plainYaml).count()

        return round(loc / plays) if plays > 0 else 0
