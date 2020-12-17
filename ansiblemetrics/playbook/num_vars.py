from ansiblemetrics.ansible_metric import AnsibleMetric


class NumVars(AnsibleMetric):
    """ This class measures the number of variables in a playbook.

    TODO add support for included and imported variables
    """

    def count(self):
        """Return the number of variables.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_vars import NumVars

            playbook = '''
            - hosts: all
              remote_user: root
              vars:
                favcolor: blue                      # 1st variable
              vars_files:                           # vars_files is not supported by this version
              - /vars/external_vars.yml
            '''

            NumVars(playbook).count()

            >> 1

        Returns
        -------
        int
            number of variables.

        """
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
