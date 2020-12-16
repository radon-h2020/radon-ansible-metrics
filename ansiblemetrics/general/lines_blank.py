from ansiblemetrics.lines_metric import LinesMetric


class LinesBlank(LinesMetric):
    """ This class measures the blank lines in a playbook"""

    def count(self):
        """Return the number of blank lines

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.lines_blank import LinesBlank

            playbook = '''
            ---
            - hosts: localhost

              tasks:
              - name: task 1
                debug:
                  msg: 'Hello'

              - name: task 2
                debug:
                  msg: 'World'
            '''

            LinesBlank(playbook).count()

            >> 2

        Returns
        -------
        int
            Number of blank lines
        """
        bloc = 0

        for line in self.yml.splitlines():
            if not line.strip():
                bloc += 1

        return bloc
