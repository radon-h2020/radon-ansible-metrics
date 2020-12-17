from ansiblemetrics.ansible_metric import AnsibleMetric


class NumPlays(AnsibleMetric):
    """ This class measures the number of plays in a playbook. """

    def count(self):
        """Return the number of plays.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_plays import NumPlays

            playbook = '''
            ---
            - hosts: all
              roles:
              - common

            - hosts: dbservers
              roles:
              - db
            '''

            NumPlays(playbook).count()

            >> 2

        Returns
        -------
        int
            number of plays

        """
        return len(self.plays)
