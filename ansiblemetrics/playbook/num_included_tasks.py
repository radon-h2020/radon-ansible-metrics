import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumIncludedTasks(AnsibleMetric):
    """ This class measures the number of included tasks in a playbook.
    """

    def count(self):
        """Return the number of included tasks.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_included_tasks import NumIncludedTasks

            playbook = '''
            - name: Include task list in play
              include_tasks: stuff.yaml
            '''

            NumIncludedTasks(playbook).count()

            >> 1

        Returns
        -------
        int
            number of included tasks

        """
        script = self.playbook
        keys = utils.all_keys(script)
        return sum(1 for i in keys if i == 'include_tasks')
