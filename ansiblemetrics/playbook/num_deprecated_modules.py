from ansiblemetrics.ansible_modules import DEPRECATED_MODULES_LIST
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumDeprecatedModules(AnsibleMetric):
    """ This class measures the number of times tasks use deprecated modules."""

    def count(self):
        """Return the deprecated modules occurrence.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_deprecated_modules import NumDeprecatedModules

            playbook = '''
            - name: Include unique username from register.yml
              include_vars:   # non deprecated module
                file: username_info.yml

            - name: Create a service
              oc:   # deprecated module
                state: present
                name: myservice
                namespace: mynamespace
                kind: Service
            '''

            NumDeprecatedModules(playbook).count()

            >> 1

        Returns
        -------
        int
            deprecated modules occurrence

        """

        modules = []

        for task in self.tasks:
            if not task:
                continue

            for key in task:
                if key in DEPRECATED_MODULES_LIST:
                    modules.append(key)

        return len(modules)
