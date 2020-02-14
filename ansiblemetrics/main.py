import inspect, os, re, yaml

from enum import Enum
from io import StringIO
from ansiblemetrics.import_metrics import general_metrics, playbook_metrics, tasks_metrics

class LoadingError(Exception):
    pass

class MetricExtractor():

    def __execute_2(self, metric, script):
        """
        Returns a triple (count, relative=None, occurrences=None) as result of the metric.
        Relative and occurrences are None by default. If the metric provides a relative or occurreces value, they will be set to their actual value
        """
        try:
            m = metric(script)
            count = m.count()
            
            relative = None
            occurrences = None

            # Check if the metric uses the argument 'relative' or 'occurrences.'
            spec = inspect.getfullargspec(m.count)
            if 'relative' in spec.args:
                relative = round(m.count(relative=True), 2)
            if 'occurrences' in spec.args:
                occurrences = round(m.count(occurrences=True), 2)

            return (count, relative, occurrences)

        except Exception:
            return (None, None, None)

    def __executeOnPlaybookTasks(self, script):
        try:
            yml = yaml.safe_load(script.getvalue())
            if yml is None:
                return {}
            
            tasks = []

            for d in yml:
                
                if type(d) != dict:
                    continue
                
                if d.get('pre_tasks') is not None:
                    tasks.extend(d.get('pre_tasks'))
                
                if d.get('tasks') is not None:
                    tasks.extend(d.get('tasks'))

            # using list comprehension to remove None values in list 
            tasks = [i for i in tasks if i] 

            if len(tasks) == 0:
                return {}
                
            tasks = StringIO(yaml.dump(tasks))
        except yaml.YAMLError:
            return {} 

        results = {}

        for name in tasks_metrics:
            metric_tuple = self.__execute_2(tasks_metrics[name], tasks)
            
            results[name] = {} 
            results[name]['count'] = metric_tuple[0]

            if metric_tuple[1] is not None:
                results[name]['count_relative'] = metric_tuple[1]
            elif metric_tuple[2] is not None:
                results[name]['count_occurrences'] = metric_tuple[2]

        return results
    
    def __execute(self, script, metrics_type='general'):
        """
        Executes metrics on a given script and returns a dictionary of results
        script: str  -- a StringIO object representing a IaC script in Ansible
        metrics: str -- possible options: 'general', 'playbook', 'tasks', 'playbook_and_general', tasks_and_general'
        """
        metrics = general_metrics
        results = {}

        if metrics_type == 'playbook':
            metrics = playbook_metrics
            results = self.__executeOnPlaybookTasks(script)
        
        elif metrics_type == 'tasks':
            metrics = tasks_metrics
        
        elif metrics_type == 'playbook_and_general':
            metrics = dict(list(general_metrics.items()) + list(playbook_metrics.items()))
            results = self.__executeOnPlaybookTasks(script)
        
        elif metrics_type == 'tasks_and_general':
            metrics = dict(list(general_metrics.items()) + list(tasks_metrics.items())) 

        
        # Execute metrics 
        for name in metrics:
            metric_tuple = self.__execute_2(metrics[name], script)

            results[name] = {}    
            results[name]['count'] = metric_tuple[0]

            if metric_tuple[1] is not None:
                results[name]['count_relative'] = metric_tuple[1]
            elif metric_tuple[2] is not None:
                results[name]['count_occurrences'] = metric_tuple[2]

        return results

    def run(self, script: StringIO):        

        if script is None:
            raise LoadingError()

        yml = None    
        try:
            yml = yaml.safe_load(script.getvalue())
        except yaml.YAMLError:
            raise yaml.YAMLError()

        if yml is None or len(yml) == 0:
            raise Exception()
        
        if type(yml) == dict:
            yml = [yml]

        i = 0

        while(i < len(yml) and yml[i].get('hosts') is None):
            i+=1 

        if i < len(yml):   # script is a playbook
            metrics = self.__execute(script, metrics_type='playbook_and_general')
        else:   # Assumed tasks file
            metrics = self.__execute(script, metrics_type='tasks_and_general')
        
        script.close()
        
        return metrics
