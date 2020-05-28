import re

from ansiblemetrics.ansible_metric import AnsibleMetric

regex = re.compile(r'\band\b | \bor\b | \bnot\b', flags=re.X)


class NumDecisions(AnsibleMetric):
    """ This class implements the metric 'Number of logic operands' in an Ansible script. """

    def count(self):

        decisions = 0

        stack = self.playbook

        while stack:
            d = stack.pop(0)

            if not d or type(d) != dict:
                continue

            for k, v in d.items():

                if k == 'when':
                    # if a string (instead of list), add to list for next steps
                    if type(v) == str:
                        v = [v]
                    elif type(v) == bool:
                        v = [str(v)]

                    for item in v:
                        decisions += len(regex.findall(str(item)))

                    # Multiple conditions that all need to be true (a logical 'and') can also be specified as a list
                    # The following line keep track of it
                    decisions += len(v) - 1

                elif isinstance(v, dict):
                    stack.append(v)
                elif isinstance(v, list):
                    stack.extend([item for item in v if type(item) == dict])

        return decisions
