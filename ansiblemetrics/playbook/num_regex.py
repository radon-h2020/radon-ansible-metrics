from ansiblemetrics.ansible_metric import AnsibleMetric


class NumRegex(AnsibleMetric):
    """ This class implements the metric 'Number of regex' in an Ansible script. """

    def count(self):
        """ Return the number of regexp in a playbook. """

        regex = 0

        for task in self.playbook:
            if not task or type(task) != dict:
                continue

            for k, v in task.items():

                if not k or not v:
                    continue

                regex += k == 'lineinfile' and 'regexp' in v

        return regex
