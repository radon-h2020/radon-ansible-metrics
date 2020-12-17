import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumIncludes(AnsibleMetric):
    """ This class measures the number of includes in a playbook.
    """

    def count(self):
        """Return the number of includes.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_includes import NumIncludes

            playbook = '''
            - name: Include a play after another play
              include: otherplays.yaml

            - name: Include task list in play
              include_role: role.yaml
            '''

            NumIncludes(playbook).count()

            >> 1

        Returns
        -------
        int
            number of includes

        """
        script = self.playbook
        keys = utils.all_keys(script)
        return sum(1 for i in keys if i == 'include')
