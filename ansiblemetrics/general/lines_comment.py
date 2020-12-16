import re
from ansiblemetrics.lines_metric import LinesMetric


class LinesComment(LinesMetric):
    """ This class measures the number of comments in a playbook"""

    def count(self):
        """Return the number of commented lines

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.lines_comments import LinesComments

            playbook = '''
            ---
            - hosts: localhost

              tasks:

              # A task to say Hello World!
              - name: task 1
                debug:
                  msg: 'Hello World!'
            '''

            LinesComments(playbook).count()

            >> 1

        Returns
        -------
        int
            Number of commented lines
        """
        cloc = 0

        for lines in self.yml.splitlines():
            comment = re.search(r'#.+', str(lines.strip()))
            if comment is not None:
                cloc += 1

        return cloc
