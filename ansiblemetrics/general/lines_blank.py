from ansiblemetrics.lines_metric import LinesMetric

class LinesBlank(LinesMetric):
    """ This class is responsible for providing the methods to count the blank lines of code (bloc) in a given .yaml file"""

    def count(self):
        bloc = 0

        for l in self.yml.splitlines():            
            if not l.strip():
                bloc += 1
             
        return bloc  