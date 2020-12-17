import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumImportedPlaybooks(AnsibleMetric):
    """ This class measures the number of imported playbooks in a playbook.
    """

    def count(self):
        """Return the number of imported playbooks.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_imported_playbooks import NumImportedPlaybooks

            playbook = '''
            - name: Include a play after another play
              import_playbook: otherplays.yml

            - name: This fails because I'm inside a play already
              import_playbook: stuff.yaml
            '''

            NumImportedPlaybooks(playbook).count()

            >> 2

        Returns
        -------
        int
            number of imported playbooks

        """
        script = self.playbook
        keys = utils.all_keys(script)
        return sum(1 for i in keys if i == 'import_playbook')
