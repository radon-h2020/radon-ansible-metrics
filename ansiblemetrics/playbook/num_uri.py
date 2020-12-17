from ansiblemetrics.ansible_metric import AnsibleMetric


class NumUri(AnsibleMetric):
    """ This class measures the number of URIs in a playbook.
    """

    def count(self):
        """Return the number of URIs

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_uri import NumUri

            playbook = '''
            - name: Check that you can connect (GET) to a page and it returns a status 200
              uri:
                url: http://www.example.com
            '''

            NumUri(playbook).count()

            >> 1

        Returns
        -------
        int
            number of URIs

        """
        return sum(1 for task in self.tasks if task and 'uri' in task)
