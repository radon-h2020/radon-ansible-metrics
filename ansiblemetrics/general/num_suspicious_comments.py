import re

from ansiblemetrics.ansible_metric import AnsibleMetric


class NumSuspiciousComments(AnsibleMetric):
    """ This class implements the metric 'Number of suspicious comments' in an Ansible script. """

    def __init__(self, script):
        """
        Initialize a new Ansible Metric.
        ymlStream -- a StringIO object representing a valid yaml file
        """
        super().__init__(script)
        self.__yml = script.getvalue()

    def count(self):
        """ Return the number of suspicious comments in the script. """

        suspicious = 0

        for l in self.__yml.splitlines():
            comment = re.search(r'#.+', str(l.strip()))
            if comment is not None:
                if re.search(r'TODO|FIXME|HACK|XXX|CHECKME|DOCME|TESTME|PENDING', comment.group()) is not None:
                    suspicious += 1

        return suspicious
