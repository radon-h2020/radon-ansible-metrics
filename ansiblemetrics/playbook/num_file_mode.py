from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.ansible_modules import FILE_MODULES


class NumFileMode(AnsibleMetric):
    """ This class measures the number of times playbook manages a file's permissions.

    File 'mode' is a source code property used to manage files, directories and symbolic links.
    """

    def count(self):
        """Return the number of file's mode syntax occurrences.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_fact_modules import NumFileMode

            playbook = '''
            - name: Change file ownership, group and permissions
              file:
                path: /etc/foo.conf
                owner: foo
                group: foo
                mode: '0644'    # 1st occurrence
            '''

            NumFileMode(playbook).count()

            >> 1

        Returns
        -------
        int
            number of file's mode syntax occurrences

        """

        n_mode = 0

        for task in self.tasks:
            if not task or type(task) != dict:
                continue

            for k, v in task.items():
                if not k or not v:
                    continue

                if k in FILE_MODULES and 'mode' in v:
                    n_mode += 1

        return n_mode
