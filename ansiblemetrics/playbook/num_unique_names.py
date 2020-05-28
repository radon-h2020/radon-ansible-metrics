import re
from collections import Counter
from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import key_value_list


class NumUniqueNames(AnsibleMetric):
    """  This class implements the metric 'Number Of Unique Names' in an Ansible script. """

    def count(self):
        """ 
        Return the number of unique names in a Ansible script. 
        """
        names = []

        for item in key_value_list(self.playbook):  # [(key, value)]
            if item[0] == 'name':
                item = re.sub(r'\s+', '', str(item[1]))
                names.append(item.strip())

        frequencies = Counter(names).values()  # counts the elements' frequency
        unique = sum(1 for v in frequencies if v == 1)

        return unique
