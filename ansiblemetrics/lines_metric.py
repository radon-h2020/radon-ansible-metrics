import yaml
from io import StringIO


class LinesMetric():
    """ This class is responsible for providing the methods to count the lines of code (loc) in a given .yaml file"""

    def __init__(self, script: StringIO):
        """
        Initialize a new LOC AnsibleMetric.
        script -- a StringIO object representing a valid yaml file
        """
        if not isinstance(script, StringIO):
            raise TypeError('Expected a StringIO object')

        try:
            # Check if is a valid yaml
            self.__yml = yaml.safe_load(script.getvalue())
            if self.__yml is None:
                raise TypeError("Expected a not empty Ansible script")

            self.__yml = script.getvalue()

        except yaml.YAMLError:
            raise TypeError("Expected a valid Ansible script")

    @property
    def yml(self):
        return self.__yml

    def count(self):
        pass
