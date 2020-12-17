import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumIncludedRoles(AnsibleMetric):
    """ This class measures the number of included roles in a playbook"""

    def count(self):
        """Return the number of included roles

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_included_roles import NumIncludedRoles

            playbook = '''
            - name: Include task list in play
              include_role: role.yaml
            '''

            NumIncludedRoles(playbook).count()

            >> 1

        Returns
        -------
        int
            number of included roles

        """
        script = self.playbook
        keys = utils.all_keys(script)
        return sum(1 for i in keys if i == 'include_role')
