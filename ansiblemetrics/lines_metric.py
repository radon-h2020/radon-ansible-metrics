import yaml

class LinesMetric:
    """ This class is responsible for providing the methods to count the lines of code (loc) in a given .yaml file"""

    def __init__(self, script: str):
        """
        Initialize a new LOC AnsibleMetric.
        script -- a plain yaml file
        """
        if script is None:
            raise TypeError("Parameter 'script' meant to be a string, not None.")

        try:
            # Check if is a valid yaml
            self.__yml = yaml.safe_load(script)
            if self.__yml is None:
                raise TypeError("Expected a not empty Ansible script")

            self.__yml = script

        except yaml.YAMLError:
            raise TypeError("Expected a valid Ansible script")

    @property
    def yml(self):
        return self.__yml

    def count(self):
        pass
