from ansiblemetrics.ansible_modules import DEPRECATED_MODULES_LIST
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumDeprecatedModules(AnsibleMetric):
    """ 
    This class implements the metric 'Number Of (default) Deprecated Modules' in a Ansible script.
    """

    def count(self):
        """ 
        Return the number of (occurrences of) deprecated modules.
        """

        modules = []

        for task in self.tasks:
            if not task:
                continue

            for key in task:
                if key in DEPRECATED_MODULES_LIST:
                    modules.append(key)

        return len(modules)
