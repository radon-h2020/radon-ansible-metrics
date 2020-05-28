from ansiblemetrics.ansible_metric import AnsibleMetric


class NumVars(AnsibleMetric):
    """ This class implements the metric 'Number Of Vars' (Variables) in an Ansible script. 
    TODO add support for included and imported variables
    """

    def count(self):
        """ Return the number of vars in a playbook. """
        stack = self.playbook
        vars = 0
        while stack:
            d = stack.pop(0)

            if not d or type(d) != dict:
                continue

            for k, v in d.items():

                if not v:
                    continue

                if k == 'vars':
                    vars += len(v)
                elif k == 'register':
                    vars += 1
                elif type(v) == dict:
                    stack.append(v)
                elif type(v) == list:
                    stack.extend([item for item in v if type(item) == dict])

        return vars
