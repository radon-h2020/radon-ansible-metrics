import re

from ansiblemetrics.utils import key_value_list
from ansiblemetrics.ansible_metric import AnsibleMetric

OPERANDS = r'\{\{\s*[0-9]+\s*(\+|-|\/\/|\/|%|\*\*|\*)\s*[0-9]+\s*\}\}'


class NumMathOperations(AnsibleMetric):
    """ This class measures the number of math operations in a playbook.
    The following operators are considered for the calculation: +, -, /, //, %, *, **.
    """

    def count(self):
        """Return the number of mathematical operations.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_math_operations import NumMathOperations

            playbook = '''
            - hosts: localhost

              tasks:
              - debug:
                  msg: "addition: {{ 4 + 3 }}"  # 1st operation
              - debug:
                  msg: "subtraction: {{ 4 - 3 }}"   # 2nd operation
              - debug:
                  msg: "multiplication: {{ 4 * 3 }}"    # 3rd operation
              - debug:
                  msg: "Modulo operation: {{ 7 % 4}}"   # 4th operation
              - debug:
                  msg: "floating division: {{ 4 / 3}}"  # 5th operation
            '''

            NumMathOperations(playbook).count()

            >> 5

        Returns
        -------
        int
            Number of math operations
        """
        return sum(len(re.findall(OPERANDS, str(v))) for k, v in key_value_list(self.playbook))
