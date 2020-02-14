import re

from ansiblemetrics.general.loc import LOC

class CLOC(LOC):
    """ This class is responsible for providing the methods to count the comments lines of code (cloc) in a given .yaml file"""

    def count(self, relative=False):
        cloc = 0

        for l in self.yml.splitlines():            
            comment = re.search(r'#.+', str(l.strip()))
            if comment is not None:   
                cloc += 1

        if relative:
            loc = super().count()
            if loc > 0:
                cloc = float(cloc)/float(loc)
             
        return cloc
        