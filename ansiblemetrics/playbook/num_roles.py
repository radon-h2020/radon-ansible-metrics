from ansiblemetrics.ansible_metric import AnsibleMetric


class NumRoles(AnsibleMetric):
    """ This class measures the number of roles in a playbook.
    """

    def count(self):
        """Return the number of roles.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_roles import NumRoles

            playbook = '''
            ---
            - hosts: all
              roles:
              - common  # 1st role

            - hosts: dbservers
              roles:
              - db  # 2nd role

            '''

            NumRoles(playbook).count()

            >> 2

        Returns
        -------
        int
            number of roles

        """

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
