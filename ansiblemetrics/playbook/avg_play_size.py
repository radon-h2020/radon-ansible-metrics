import yaml

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.general.lines_code import LinesCode
from ansiblemetrics.playbook.num_plays import NumPlays


class AveragePlaySize(AnsibleMetric):
    """ This class implements the metric 'Average Play Size' in an Ansible script. """

    def count(self):
        plain_yaml = yaml.dump(self.playbook)
        loc = LinesCode(plain_yaml).count()
        plays = NumPlays(plain_yaml).count()

        return round(loc / plays) if plays > 0 else 0
