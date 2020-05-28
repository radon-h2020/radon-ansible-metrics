import yaml
from io import StringIO


class AnsibleMetric():

    def __init__(self, script: StringIO):
        """
        Initialize a new Ansible AnsibleMetric.
        script -- a StringIO object representing the script or the tasks file to parse
        """
        if not isinstance(script, StringIO):
            raise TypeError('Expected a StringIO object')

        try:
            self.__yml = yaml.safe_load(script.getvalue())
            if self.__yml is None:
                raise TypeError("Expected a not empty Ansible script")

            if type(self.__yml) != list:
                self.__yml = [self.__yml]

        except yaml.YAMLError:
            raise TypeError("Expected a valid Ansible script")

    @property
    def playbook(self):
        """
        Always return a list of items.
        If the yml is a single dictionary, then it return a list of one dictionary [self.__yml]
        """
        return self.__yml

    @property
    def plays(self):
        if any('hosts' in d.keys() for d in self.__yml if type(d) == dict):
            return self.__yml
        else:
            return list()

    @property
    def tasks(self):

        if self.plays:
            tasks = list()
            for play in self.plays:
                if 'tasks' in play:
                    tasks.extend(play['tasks'])

            return tasks
        else:
            return self.playbook

    def count(self):
        pass  # implementation not provided for the parent class
