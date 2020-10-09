import re

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import key_value_list

filter_regex = re.compile(r'[^\|]+(\|)[^\|]')


class NumFilters(AnsibleMetric):
    """ This class implements the metric 'Number Of Filters' in an Ansible script. """

    def count(self):
        """  Return the number of filters. """
        filters = 0

        for item in key_value_list(self.playbook):
            v = item[1]
            if v is not None and re.search(r'\{\{.*\}\}', str(
                    v)) is not None:  # check for statements with brackets, such as: {{ foobar }}
                filters += len(filter_regex.findall(str(v)))

        return filters
