import re

from ansiblemetrics.utils import key_value_list
from ansiblemetrics.ansible_metric import AnsibleMetric

COMPARISON_OPERATORS = re.compile(r'\bis\b|\bin\b|\bnot\b|==|!=|>=|>|<=|<')


class NumConditions(AnsibleMetric):
    """ This class measures the number of conditions in a playbook

    A condition is a Boolean expression containing no Boolean operators.
    Conditions are identified by the following comparison operators: is, in, ==, !=, >, >=, <, <=.
    """

    def count(self):
        """Return the number of conditions.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_conditions import NumConditions

            playbook = '''
            - hosts: all
              vars:
              - hello_msg: "Hello World"

              tasks:
              - debug:
                  msg: "Equals"
                  when:
                    - "Hello" in hello_msg    # 1st condition
                    - "World" in hello_msg    # 2nd condition
            '''

            NumConditions(playbook).count()

            >> 2

        Returns
        -------
        int
            Number of conditions
        """

        conditions = 0
        for k, v in key_value_list(self.playbook):
            if k not in ('when', 'changed_when', 'failed_when') or v is None:
                continue

            if type(v) == bool:
                conditions += 1
            else:
                conditions += len(COMPARISON_OPERATORS.findall(str(v)))

        return conditions
