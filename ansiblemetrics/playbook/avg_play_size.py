import yaml

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.general.lines_code import LinesCode
from ansiblemetrics.playbook.num_plays import NumPlays


class AvgPlaySize(AnsibleMetric):
    """ This class measures a play's average number of lines of code."""

    def count(self):
        """Return the average play size.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.avg_play_size import AvgPlaySize

            playbook = '''
            ---
            # 1st play
            - hosts: all
              roles:
              - common

            # 2nd play
            - hosts: monitoring
              roles:
              - base-apache
              - nagios
            '''

            AvgPlaySize(playbook).count()

            >> 4

        Returns
        -------
        int
            Average play size, rounded to the nearest unit
        """
        plain_yaml = yaml.dump(self.playbook)
        loc = LinesCode(plain_yaml).count()
        plays = NumPlays(plain_yaml).count()

        return round(loc / plays) if plays > 0 else 0
