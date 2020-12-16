import yaml


class LinesMetric:
    """ This is an abstract class the concrete classes measuring lines of code will extend.
    """

    def __init__(self, script: str):
        """The class constructor.

        Parameters
        ----------
        script : str
            A plain Ansible file

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
        """The plain Ansible file
        """
        return self.__yml

    def count(self):
        """Method to execute the metric.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.lines_metric import LinesMetric
            LinesMetric().count()
        """
        pass
