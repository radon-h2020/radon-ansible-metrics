import re

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import key_value_list

filter_regex = re.compile(r'[^\|]+(\|)[^\|]')


class NumFilters(AnsibleMetric):
    """ This class measures the number of filters in a playbook.
    """

    def count(self):
        """Return the number of filters.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_filters import NumFilters

            playbook = '''
            - shell: cat /some/path/to/multidoc-file.yaml
              register: result
            - debug:
                msg: '{{ item }}'
              loop: '{{ result.stdout | from_yaml_all | list }}'  # 2 filters
            '''

            NumFilters(playbook).count()

            >> 2

        Returns
        -------
        int
            number of filters

        """
        filters = 0

        for item in key_value_list(self.playbook):
            v = item[1]
            if v is not None and re.search(r'\{\{.*\}\}', str(
                    v)) is not None:  # check for statements with brackets, such as: {{ foobar }}
                filters += len(filter_regex.findall(str(v)))

        return filters
