from ansiblemetrics.ansible_metric import AnsibleMetric


class NumRegex(AnsibleMetric):
    """ This class measures the number of regular expressions in a playbook.
    """

    def count(self):
        """Return the number of regular expressions.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_regex import NumRegex

            playbook = '''
            ---
            - name: Remove Password
              lineinfile:
                path: "/opt/appdata/nzbget/nzbget.conf"
                regexp: ControlPassword=tegbzn6789
                line: 'ControlPassword='
                state: present
              when: nzbget_conf.stat.exists == False
            '''

            NumRegex(playbook).count()

            >> 1

        Returns
        -------
        int
            number of regular expressions

        """

        regex = 0

        for task in self.playbook:
            if not task or type(task) != dict:
                continue

            for k, v in task.items():

                if not k or not v:
                    continue

                regex += k == 'lineinfile' and 'regexp' in v

        return regex
