from ansiblemetrics.ansible_modules import ANSIBLE_MODULES_LIST
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumDistinctModules(AnsibleMetric):
    """ This class measures the number of distinct modules in the script.

    It  differs from ansiblemetrics.playbook.NumTasks as it counts the number of distinct modules in the script without
    duplicates.
    If a module occurs twice or more among tasks it is counted only once.
    Recall that the goal of a task is to execute a module, so the total number of modules (with duplicates) equals the
    number of tasks.

    """

    def count(self):
        """Return the number of distinct modules.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_distinct_modules import NumDistinctModules

            playbook = '''
            - name: Include username_info
              include_vars:  # module
                file: username_info.yml

            - name: Include settings_info
              include_vars:  # module
                file: settings_info.yml

            - name: Grab HUE light info
              uri:  # module
                url: "http://{{ip_address}}/api/{{username}}"
                method: GET
                body: '{{body_info|to_json}}'
            '''

            NumDistinctModules(playbook).count()

            >> 2

        Returns
        -------
        int
            number of distinct modules

        """
        modules = 0
        for task in self.tasks:
            if not task:
                continue

            if any(k in ANSIBLE_MODULES_LIST for k in task):
                modules += 1

        return modules
