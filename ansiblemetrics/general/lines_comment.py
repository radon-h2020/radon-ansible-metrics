import re
from ansiblemetrics.lines_metric import LinesMetric

class LinesComment(LinesMetric):
    """ This class is responsible for providing the methods to count the comments lines of code (cloc) in a given .yaml file"""

    def count(self):
        cloc = 0

        for l in self.yml.splitlines():            
            comment = re.search(r'#.+', str(l.strip()))
            if comment is not None:   
                cloc += 1

        return cloc
        