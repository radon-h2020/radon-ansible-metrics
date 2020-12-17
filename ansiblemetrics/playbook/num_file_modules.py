from ansiblemetrics.ansible_metric import AnsibleMetric


class NumFileModules(AnsibleMetric):
    """ This class measures the occurrences of the file module in a playbook.

    The file module is used to manage files and their properties.
    """

    def count(self):
        """Return the file module occurrences.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_file_modules import NumFileModules

            playbook = '''
            - name: Change file ownership, group and permissions
              file:    # 1st occurrence
                path: /etc/foo.conf
                owner: foo
                group: foo
                mode: '0644'
            '''

            NumFileModules(playbook).count()

            >> 1

        Returns
        -------
        int
            number of file module occurrences

        """
        return sum(1 for task in self.tasks if task and 'file' in task)
