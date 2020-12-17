import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumImportedTasks(AnsibleMetric):
    """ This class measures the number of imported tasks list in a playbook.
    """

    def count(self):
        """Return the number of imported tasks.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_imported_tasks import NumImportedTasks

            playbook = '''
            - name: Include task list in play
              import_tasks: stuff.yaml
            '''

            NumImportedTasks(playbook).count()

            >> 1

        Returns
        -------
        int
            number of imported tasks

        """
        script = self.playbook
        keys = utils.all_keys(script)
        return sum(1 for i in keys if i == 'import_tasks')
