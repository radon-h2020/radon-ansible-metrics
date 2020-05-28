from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.ansible_modules import ANSIBLE_MODULES_LIST


class NumParameters(AnsibleMetric):
    """ This class implements the metric 'Number of parameters in an Ansible script. """

    def count(self):
        """ Count the number of parameters """

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
