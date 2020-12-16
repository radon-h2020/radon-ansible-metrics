import re

from ansiblemetrics.ansible_metric import AnsibleMetric

regex = re.compile(r'\band\b | \bor\b | \bnot\b', flags=re.X)


class NumDecisions(AnsibleMetric):
    """ This class implements the metric 'Number of decisions' in an Ansible script.

    A decision is a Boolean expression composed of conditions and one or more Boolean operators.
    Decisions are identified by the following logical operators: ```and, or, not```.
    """

    def count(self):
        """Return the number of decisions.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_decisions import NumDecisions

            playbook = '''
            - hosts: all
              vars:
              - hello_msg: "Hello World"

              tasks:
              - debug:
                  msg: "{{ hello_msg }}"
                when: "Hello" in hello_msg and "World" in hello_msg   # 1st decision

              - debug:
                  msg: "Goodbye World"
                when:
                    - "World" in hello_msg and not "Hello" in hello_msg    # 2nd (and) and 3rd (not) decision
            '''

            NumDecisions(playbook).count()

            >> 3

        Returns
        -------
        int
            Number of decisions
        """

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
