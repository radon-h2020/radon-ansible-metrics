import yaml


class AnsibleMetric:

    def __init__(self, script: str):
        """The class constructor.

        Parameters
        ----------
        script : str
            A plain Ansible file

        Raises
        ------
        TypeError
            If the script is empty or an invalid YAML file
        """

        if script is None:
            raise TypeError("Parameter 'script' meant to be a string, not None.")

        try:
            self.__yml = yaml.safe_load(script)
            if self.__yml is None:
                raise TypeError("Expected a not empty Ansible script")

            if type(self.__yml) != list:
                self.__yml = [self.__yml]

        except yaml.YAMLError:
            raise TypeError("Expected a valid Ansible script")

    @property
    def playbook(self):
        """The list of items plays and tasks in the playbook
        """
        return self.__yml

    @property
    def plays(self):
        """The list of plays in the playbook
        """

        if any('hosts' in d.keys() for d in self.__yml if type(d) == dict):
            return self.__yml
        else:
            return list()

    @property
    def tasks(self):
        """The list of tasks in the playbook.
        """

        if self.plays:
            tasks = list()
            for play in self.plays:
                if 'tasks' in play:
                    tasks.extend(play['tasks'])

            return tasks
        else:
            return self.playbook

    def count(self):
        """Method to execute the metric.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.ansible_metric import AnsibleMetric
            AnsibleMetric().count()
        """
        pass
