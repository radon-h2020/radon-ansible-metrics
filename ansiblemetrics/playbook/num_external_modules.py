from ansiblemetrics.ansible_modules import ANSIBLE_MODULES_LIST
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumExternalModules(AnsibleMetric):
    """ 
    This class implements the metric 'Number Of External Modules' in an Ansible script.
    External modules are modules that do not belong to the core Ansible modules or are not maintained by the Ansible community.
    """

    def count(self):
        """ Return the number of external modules"""

        external = 0

        for task in self.tasks:
            if not task:
                continue

            if not any(k in ANSIBLE_MODULES_LIST for k in task):
                external += 1

        return external
