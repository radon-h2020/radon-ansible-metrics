import re

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import key_value_list


class NumLookups(AnsibleMetric):
    """ This class measures the number of lookups in a playbook.

    Lookups are evaluated when the task referencing them is executed, which allows for dynamic data discovery.
    To reuse a particular lookup in multiple tasks and re-evaluate it each time, a playbook variable can be defined
    with a lookup value. Each time the playbook variable is referenced the lookup will be executed, potentially
    providing different values over time.

    """

    def count(self):
        """Return the number of lookups.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_lookups import NumLookups

            playbook = '''
            - hosts: all
              vars:
                contents: "{{ lookup('file', '/etc/foo.txt') }}"
            '''

            NumLookups(playbook).count()

            >> 1

        Returns
        -------
        int
            number of lookups

        """
        lookups = 0

        for item in key_value_list(self.playbook):
            v = item[1]
            if re.search(r'\{\{\s*lookup\(.*\)\s*\}\}', str(v)) is not None:
                lookups += 1

        return lookups
