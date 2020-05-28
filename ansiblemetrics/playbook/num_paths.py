from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.ansible_modules import ANSIBLE_MODULES_LIST


class NumPaths(AnsibleMetric):
    """ This class implements the metric 'Number of paths' in an Ansible script. """

    def count(self):
        """ Return the number of path, src and dest in a playbook. """

        paths = 0
        for task in self.tasks:
            if not task or type(task) != dict:
                continue

            for k, v in task.items():

                if not k or not v:
                    continue

                if k in ANSIBLE_MODULES_LIST and type(v) == dict:
                    paths += sum(map(lambda x: x == 'path' or x == 'src' or x == 'dest', v))

        return paths
