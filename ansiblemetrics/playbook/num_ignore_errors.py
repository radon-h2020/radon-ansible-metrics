from ansiblemetrics.ansible_metric import AnsibleMetric


class NumIgnoreErrors(AnsibleMetric):
    """ This class measures the number of times a playbook ignore errors through the property ignore_errors.

    Ignoring errors is considered as a bad practice, since ignore errors only obscures error handling.
    There are better ways for handling errors. See https://blog.newrelic.com/engineering/ansible-best-practices-guide/
    for more details.
    """

    def count(self):
        """Return the number of ignore_errors: yes/True.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_ignore_errors import NumIgnoreErrors

            playbook = '''
            - name: this will not be counted as a failure
              command: /bin/false
              ignore_errors: yes
            '''

            NumIgnoreErrors(playbook).count()

            >> 1

        Returns
        -------
        int
            number of ignore_errors set to True or yes

        """

        ignore_errors = 0
        for task in self.tasks:
            if not task:
                continue

            if 'ignore_errors' in task and task['ignore_errors'] in ('yes', True):
                ignore_errors += 1

        return ignore_errors
