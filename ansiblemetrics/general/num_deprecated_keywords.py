import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_keywords import DEPRECATED_KEYWORDS
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumDeprecatedKeywords(AnsibleMetric):
    """ This class implements the metric 'Number Of Deprecated Keywords' in an Ansible script """

    def count(self):
        """ 
        Returns the number of deprecated keywords in the script 
        """
        deprecated = []

        keys = utils.all_keys(self.playbook)

        for k in keys:
            if k in DEPRECATED_KEYWORDS:
                deprecated.append(k)

        return len(deprecated)
