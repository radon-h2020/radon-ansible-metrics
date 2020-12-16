import re

from ansiblemetrics.lines_metric import LinesMetric


class NumSuspiciousComments(LinesMetric):
    """ This class measures the number of suspicious comments in a playbook.

    Suspicious comments contain at least one of the following keywords: TODO, FIXME, HACK, XXX, CHECKME, DOCME, TESTME, PENDING.
    """

    def count(self):
        """Return the number of suspicious comments.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_suspicious_comments import NumSuspiciousComments

            playbook = '''
            ---
            # TODO: Remove this task after Ansible 2.x npm module bug is fixed. See:
            # https://github.com/ansible/ansible-modules-extras/issues/1375
            - name: Ensure forever is installed (to run Node.js apps).
              npm: name=forever global=yes state=present
              become: yes
              become_user: "{{ nodejs_install_npm_user }}"
              when: nodejs_forever
            '''

            NumSuspiciousComments(playbook).count()

            >> 1

        Returns
        -------
        int
            Number of suspicious comments
        """

        suspicious = 0

        for line in self.yml.splitlines():
            comment = re.search(r'#.+', str(line.strip()))
            if comment is not None:
                if re.search(r'TODO|FIXME|HACK|XXX|CHECKME|DOCME|TESTME|PENDING', comment.group()) is not None:
                    suspicious += 1

        return suspicious
