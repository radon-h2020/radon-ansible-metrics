import re

import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumTokens(AnsibleMetric):
    """ This class measures the number of tokens (separated by blank spaces) in a playbook. """

    def count(self):
        """Return the number of tokens.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_tokens import NumTokens

            playbook = '''
            - hosts: all

              tasks:
              - debug:
                  msg: "Hello World"
            '''

            NumTokens(playbook).count()

            >> 7

        Returns
        -------
        int
            Number of tokens
        """
        keys = len(utils.all_keys(self.playbook))
        values = utils.all_values(self.playbook)
        return keys + sum(len(re.split(r'\s+', str(value).strip())) for value in values)
