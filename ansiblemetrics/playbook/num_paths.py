from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.ansible_modules import ANSIBLE_MODULES_LIST


class NumPaths(AnsibleMetric):
    """ This class measures the number of paths in a playbook.

    Paths are identified by analyzing the parameters path, src, dest
    """

    def count(self):
        """Return the number of paths.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_paths import NumPaths

            playbook = '''
            ---
            - name: "Downloading {{program_var.stdout}} from Google Drive"
              synchronize:
                src: "/mnt/gdrive/plexguide/backup/{{program_var.stdout}.tar"
                dest: "/tmp"
            '''

            NumPaths(playbook).count()

            >> 1

        Returns
        -------
        int
            number of paths

        """

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
