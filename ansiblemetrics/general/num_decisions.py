import re

from ansiblemetrics.ansible_metric import AnsibleMetric

regex = re.compile(r'\band\b | \bor\b | \bnot\b', flags=re.X)


class NumDecisions(AnsibleMetric):
    """ This class implements the metric 'Number of decisions' in an Ansible script. """

    def count(self):

        decisions = 0

        stack = self.playbook

        while stack:
            d = stack.pop(0)

            if not d or type(d) != dict:
                continue

            for k, v in d.items():

                if k in ('when', 'changed_when', 'failed_when'):

                    if type(v) == str:
                        decisions += len(regex.findall(v))
                    if type(v) == list:
                        stack.extend({k: item} for item in v)
                        decisions += len(v) - 1

                elif isinstance(v, dict):
                    stack.append(v)
                elif isinstance(v, list):
                    stack.extend([item for item in v if type(item) == dict])

        return decisions
