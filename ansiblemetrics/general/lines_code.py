from ansiblemetrics.lines_metric import LinesMetric


class LinesCode(LinesMetric):
    """ This class measures the number of executable lines of code in a playbook.
    """

    def count(self):
        """Return the number of executable lines of code.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.lines_code import LinesCode

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

            LinesCode(playbook).count()

            >> 8

        Returns
        -------
        int
            Number of lines of code
        """
        loc = 0
        for line in self.yml.splitlines():
            if line.strip() and line.strip() != '---' and line.strip() != '-' and not line.strip().startswith('#'):
                loc += 1

        return loc
