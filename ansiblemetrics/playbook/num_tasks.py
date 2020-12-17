from ansiblemetrics.ansible_metric import AnsibleMetric


class NumTasks(AnsibleMetric):
    """ This class measures the number of tasks in a playbook.
    """

    def count(self):
        """Return the number of tasks.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_tasks import NumTasks

            playbook = '''
            - name: Say Hello
              debug:
                msg: "Hello"

            - name: Say World!
              debug:
                msg: "World!"
            '''

            NumTasks(playbook).count()

            >> 2

        Returns
        -------
        int
            number of tasks

        """
        return len(self.tasks)
