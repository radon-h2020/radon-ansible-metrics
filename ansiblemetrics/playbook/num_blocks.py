from ansiblemetrics.ansible_metric import AnsibleMetric

class NumBlocks(AnsibleMetric):
    """ This class implements the metric 'Number Of Blocks' in an Ansible script. """

    def count(self):
        """ Return the number of blocks. """
        blocks = 0

        for task in self.playbook:
            if task and 'block' in task:
                blocks += 1
                        
        return blocks