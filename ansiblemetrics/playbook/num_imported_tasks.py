import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumImportTasks(AnsibleMetric):
    """ This class measures the number of imported tasks in a playbook"""

    def count(self):
        script = self.playbook
        keys = utils.all_keys(script)
        return sum(1 for i in keys if i == 'import_tasks')
