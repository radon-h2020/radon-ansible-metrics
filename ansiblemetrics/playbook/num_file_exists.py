import re

from ansiblemetrics.ansible_metric import AnsibleMetric


class NumFileExists(AnsibleMetric):
    """ This class measures the number of time a playbook checks the existence of a file.

    In particular, the module stat retrieves facts for a file similar to the Linux/Unix stat command, and can be used to
    check for the existence of a file or directory.

    This property is measured by counting the matches of the following regular expression:

    *.(win_)?stat.* is (not)? defined

    to check if the file or directory exist.
    """

    def count(self):
        """Return the number of file existence checks.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_fact_modules import NumFileExists

            playbook = '''
            - stat:
                path: /path/to/something
              register: sym

            - debug:
                msg: "islnk isn't defined (path doesn't exist)"
              when: sym.stat.islnk is not defined  # file existence check
            '''

            NumFileExists(playbook).count()

            >> 1

        Returns
        -------
        int
            number of file existence checks

        """

        n_checks = 0

        for task in self.tasks:
            if not task or type(task) != dict:
                continue

            for k, v in task.items():
                if not k or not v:
                    continue

                if k == 'when' and re.match(r'\w+\.(win_)?stat\.\w+\s+is\s*(not)?\s*defined', str(v)):
                    n_checks += 1

        return n_checks
