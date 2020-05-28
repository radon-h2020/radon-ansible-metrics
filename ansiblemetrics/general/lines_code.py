from ansiblemetrics.lines_metric import LinesMetric


class LinesCode(LinesMetric):
    """ This class is responsible for providing the methods to count the lines of code (loc) in a given YAML file"""

    def count(self):
        loc = 0
        for l in self.yml.splitlines():
            if l.strip() and l.strip() != '---' and l.strip() != '-' and not l.strip().startswith('#'):
                loc += 1

        return loc
