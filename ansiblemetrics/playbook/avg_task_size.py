import yaml

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.general.lines_code import LinesCode


class AvgTaskSize(AnsibleMetric):
    """ This class measures a task's average number of lines of code. """

    def count(self):
        """Return the average task size.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.avg_task_size import AvgTaskSize

            playbook = '''
            ---
            - name: 1st task
              include_vars:
                file: username_info.yml

            - name: 2nd task
              uri:
                url: "http://{{ip_address}}/api/{{username}}"
                method: GET
                body: '{{body_info|to_json}}'
              register: light_info

            - name: 3rd task
              debug:
                var: light_info.json.lights
            '''

            AvgTaskSize(playbook).count()

            >> 4

        Returns
        -------
        int
            Average task size, rounded to the nearest unit
        """

        size = 0
        n_tasks = 0
        for task in self.tasks:
            if not task:
                continue

            n_tasks += 1
            size += LinesCode(yaml.dump(task)).count()

        return int(round(size / n_tasks)) if n_tasks else 0
