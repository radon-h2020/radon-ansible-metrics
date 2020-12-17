from ansiblemetrics.ansible_modules import ANSIBLE_MODULES_LIST
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumExternalModules(AnsibleMetric):
    """ This class measures the number of modules in a playbook that do not belong to the core Ansible modules or are
    not maintained by the Ansible community.

    """

    def count(self):
        """Return the number of external modules.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_external_modules import NumExternalModules

            playbook = '''
            - name: ensure foo
              file:   # Core module
                path: /tmp/foo
                state: touch

            - name: do a remote copy
              remote_copy:    # External module
                source: /tmp/foo
                dest: /tmp/bar
            '''

            NumExternalModules(playbook).count()

            >> 1

        Returns
        -------
        int
            number of external modules

        """

        external = 0

        for task in self.tasks:
            if not task:
                continue

            if not any(k in ANSIBLE_MODULES_LIST for k in task):
                external += 1

        return external
