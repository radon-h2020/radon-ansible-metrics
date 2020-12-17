import re
from collections import Counter
from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import key_value_list


class NumUniqueNames(AnsibleMetric):
    """ This class measures the number of plays and tasks with unique a name.
    """

    def count(self):
        """Return the number of plays and tasks with a unique name.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_unique_names import NumUniqueNames

            playbook = '''
            ---
            - name: demo the logic                    # unique name
              hosts: localhost
              gather_facts: false
              vars:
                num1: 10
                num3: 10

              tasks:
              - name: logic and comparison            # duplicate
                debug:
                  msg: "Can you read me?"
                when: num1 >= num3 and num1 is even and num2 is not defined

              - name: logic and comparison            # duplicate
                debug:
                  msg: "Can you read me again?"
                when: num3 >= num1
            '''

            NumUniqueNames(playbook).count()

            >> 1

        Returns
        -------
        int
            number of plays and tasks with a unique name

        """
        names = []

        for item in key_value_list(self.playbook):  # [(key, value)]
            if item[0] == 'name':
                item = re.sub(r'\s+', '', str(item[1]))
                names.append(item.strip())

        frequencies = Counter(names).values()  # counts the elements' frequency
        unique = sum(1 for v in frequencies if v == 1)

        return unique
