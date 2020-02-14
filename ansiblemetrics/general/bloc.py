from ansiblemetrics.general.loc import LOC

class BLOC(LOC):
    """ This class is responsible for providing the methods to count the blank lines of code (bloc) in a given .yaml file"""

    def count(self, relative=False):
        bloc = 0

        for l in self.yml.splitlines():            
            if not l.strip():
                bloc += 1

        if relative:
            loc = super().count()
            if loc > 0:
                bloc = float(bloc)/float(loc)
             
        return bloc  