import yaml
from io import StringIO
from ansiblemetrics.exceptions import NotPlaybookError, NotStringIOError

class AnsibleMetric():

    def __init__(self, script):
        """
        Initialize a new Ansible AnsibleMetric.
        script -- a StringIO object representing the script or the tasks file to parse
        """
        if not isinstance(script, StringIO):
            raise NotStringIOError

        try:
            self.__yml = yaml.safe_load(script.getvalue())
            if self.__yml is None:
                raise NotPlaybookError("Expected a not empy Ansible script")
        except yaml.YAMLError as e:
            raise NotPlaybookError("Expected a valid Ansible script")

    @property
    def yml(self):
        return self.__yml

    def count(self):
        pass        # implementation not provided for the parent class