import inspect, os, re, yaml

from enum import Enum
from io import StringIO
from ansiblemetrics.import_metrics import general_metrics, playbook_metrics

class MetricExtractor():

    def __execute(self, script: StringIO):
        """
        Executes metrics on a given script and returns a dictionary of results
        script: StringIO  -- playbook or task list
        TODO: Add support for pre-tasks
        """
        metrics = general_metrics
        metrics.update(playbook_metrics)
        results = {}

        # Execute metrics 
        for name in metrics:
            try:
                results[name] = metrics[name](script).count()
            except Exception as e:
                print('\033[91m' + str(e) + '\033[0m')

        return results

    def run(self, script: StringIO):        

        if script is None:
            raise TypeError('Expected a StringIO object')

        yml = None    
        try:
            yml = yaml.safe_load(script.getvalue())
        except yaml.YAMLError:
            raise yaml.YAMLError()

        if yml is None or len(yml) == 0:
            raise ValueError('YML file is empty')
        
        metrics = self.__execute(script)
        script.close()

        return metrics

