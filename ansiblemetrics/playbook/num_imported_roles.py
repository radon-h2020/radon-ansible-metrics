import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumImportedRoles(AnsibleMetric):
    """ This class measures the number of imported roles in a playbook.
    """

    def count(self):
        """Return the number of imported roles.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_import_roles import NumImportedRoles

            playbook = '''
            - import_role:
                name: myrole

            - name: Run tasks/other.yaml instead of "main"
              import_role:
                name: myrole
                tasks_from: other
            '''

            NumImportedRoles(playbook).count()

            >> 2

        Returns
        -------
        int
            number of imported roles

        """
        script = self.playbook
        keys = utils.all_keys(script)
        return sum(1 for i in keys if i == 'import_role')
