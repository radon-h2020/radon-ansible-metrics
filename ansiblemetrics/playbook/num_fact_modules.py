from ansiblemetrics.ansible_modules import FACT_MODULES_LIST
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumFactModules(AnsibleMetric):
    """ This class measures the number of fact modules in a playbook.

    Fact modules are modules that do not alter state but rather return data.
    Knowing the number of fact modules in a playbook could represent a measure of the responsibility of the playbook.
    The assumption is that the lower the fact modules wrt the total number of modules in the script,
    the more unstable is the class behaviour, as the other modules alter its state.
    """

    def count(self):
        """Return the number of external modules.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_fact_modules import NumFactModules

            playbook = '''
            - name: Find all instances in the specified region
              ali_instance_facts:   # Fact module
                alicloud_access_key: "{{ alicloud_access_key }}"
                alicloud_secret_key: "{{ alicloud_secret_key }}"
                alicloud_region: '{{ alicloud_region }}'
              register: all_instances

            - name: Print data to terminal window
              debug:    # not fact module
                msg: 'End of tasks'
            '''

            NumFactModules(playbook).count()

            >> 1

        Returns
        -------
        int
            number of external modules

        """
        facts_modules = 0

        for task in self.tasks:
            if not task:
                continue

            if any(k in FACT_MODULES_LIST for k in task):
                facts_modules += 1

        return facts_modules
