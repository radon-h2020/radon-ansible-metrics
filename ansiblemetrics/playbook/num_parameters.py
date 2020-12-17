from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.ansible_modules import ANSIBLE_MODULES_LIST


class NumParameters(AnsibleMetric):
    """ This class measures the number of parameters in a playbook.

    Modules in Ansible have paramaters that describe the desired state of the module;
    each parameter handles some aspect of the module.
    For example, the module file has a mode parameter that specifies the permissions for the file.

    """

    def count(self):
        """Return the number of modules parameters.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_parameters import NumParameters

            playbook = '''
            - name: Create two hard links
              file:
                src: '/tmp/foo'
                dest: '/tmp/bar'
                state: hard
            '''

            NumParameters(playbook).count()

            >> 3

        Returns
        -------
        int
            number of modules parameters

        """

        n_params = 0

        for task in self.tasks:
            if not task or type(task) != dict:
                continue

            for k, v in task.items():
                if not k or not v:
                    continue

                if k in ANSIBLE_MODULES_LIST and type(v) == dict:
                    n_params += len(v)

        return n_params
