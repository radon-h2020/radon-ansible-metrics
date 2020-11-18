import re

from ansiblemetrics.utils import key_value_list
from ansiblemetrics.ansible_metric import AnsibleMetric

COMPARISON_OPERATORS = re.compile(r'\bis\b|\bin\b|\bnot\b|==|!=|>=|>|<=|<')


class NumConditions(AnsibleMetric):
    """ This class implements the metric 'Number of comparison operands' in an Ansible script. """

    def count(self):

        conditions = 0
        for k, v in key_value_list(self.playbook):
            if k not in ('when', 'changed_when', 'failed_when') or v is None:
                continue

            if type(v) == bool:
                conditions += 1
            else:
                conditions += len(COMPARISON_OPERATORS.findall(str(v)))

        return conditions
