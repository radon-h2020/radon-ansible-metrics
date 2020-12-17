import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumIncludedVars(AnsibleMetric):
    """ This class measures the number of included variables in a playbook.
    """

    def count(self):
        """Return the number of included variables.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_included_vars import NumIncludedVars

            playbook = '''
            - name: Include a play after another play
              include_vars: myvars.yaml
            '''

            NumIncludedVars(playbook).count()

            >> 1

        Returns
        -------
        int
            number of included variables

        """
        script = self.playbook
        keys = utils.all_keys(script)
        return sum(1 for i in keys if i == 'include_vars')
