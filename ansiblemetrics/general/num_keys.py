import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumKeys(AnsibleMetric):
    """ A playbook is YAML-based, and is treated as a dictionary.
    This class measures the number of keys in the dictionary representing the playbook
    """

    def count(self):
        """Return the number of keys of the dictionary representing the playbook.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_keys import NumKeys

            playbook = '''
            - hosts: all

              tasks:
              - debug:
                  msg: "Hello World"
            '''

            NumKeys(playbook).count()

            >> 4

        Returns
        -------
        int
            Number of keys
        """
        return len(utils.all_keys(self.playbook))
