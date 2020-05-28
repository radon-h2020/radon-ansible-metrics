from ansiblemetrics.ansible_modules import ANSIBLE_MODULES_LIST
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumDistinctModules(AnsibleMetric):
    """ 
    This class implements the metric 'Number Of (distinct default) Modules' in an Ansible script.
    Default modules are those maintained by the Ansible community.
    """

    def count(self):
        """ Counts the number of distinct default modules."""
        modules = 0
        for task in self.tasks:
            if not task:
                continue

            if any(k in ANSIBLE_MODULES_LIST for k in task):
                modules += 1

        return modules
