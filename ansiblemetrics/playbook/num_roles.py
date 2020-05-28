from ansiblemetrics.ansible_metric import AnsibleMetric


class NumRoles(AnsibleMetric):
    """ This class implements the metric 'Number Of Roles' in an Ansible script. """

    def count(self):
        """ Counts the number of roles in a playbook."""

        stack = self.playbook
        roles = set()

        while stack:
            d = stack.pop(0)

            if not d or type(d) != dict:
                continue

            for k, v in d.items():
                if k == 'roles':
                    for item in v:
                        if type(item) == dict:
                            stack.append(item)
                        else:
                            roles.add(item)

                elif k == 'role':
                    roles.add(v)
                elif type(v) == dict:
                    stack.append(v)
                elif type(v) == list:
                    stack.extend([item for item in v if type(item) == dict])

        return len(roles)
