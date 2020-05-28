from ansiblemetrics.ansible_modules import FACT_MODULES_LIST
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumFactModules(AnsibleMetric):
    """ This class implements the metric 'Number Of Fact Modules' in an Ansible script. """

    def count(self):
        """ Return the number of fact modules in a playbook. """
        facts_modules = 0

        for task in self.tasks:
            if not task:
                continue

            if any(k in FACT_MODULES_LIST for k in task):
                facts_modules += 1

        return facts_modules
