import yaml
from io import StringIO
from ansiblemetrics.exceptions import NotStringIOError

class LOC():
    """ This class is responsible for providing the methods to count the lines of code (loc) in a given .yaml file"""

    def __init__(self, ymlStream):
        """
        Initialize a new LOC AnsibleMetric.
        ymlStream -- a StringIO object representing a valid yaml file
        """
        if not isinstance(ymlStream, StringIO):
            raise NotStringIOError

        try:
            # Check if is a valid yaml
            self.__yml = yaml.safe_load(ymlStream.getvalue())
            if self.__yml is None:
                raise yaml.YAMLError
            
            self.__yml = ymlStream.getvalue()

        except yaml.YAMLError:
            raise yaml.YAMLError

    def count(self):
        loc = 0

        for l in self.__yml.splitlines():            
            if l.strip() and l.strip() != '---' and l.strip() != '-' and not l.strip().startswith('#'):
                loc += 1
                
        return loc

    @property
    def yml(self):
        return self.__yml