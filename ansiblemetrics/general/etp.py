from math import log2

import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric

class ETP(AnsibleMetric):
    """ This class implements the metric 'Text Entropy' of an Ansible script. """
    # TODO apply cleaning and stemming
    
    def count(self):
        
        keys = utils.allKeys(self.yml)
        values = utils.allValues(self.yml)
        
        words = keys

        for v in values:
            words.extend(str(v).split())

        wordset = set(words)
        freq={word: words.count(word) for word in wordset}

        entropy = 0
        for word in wordset:
            p = freq[word] / len(words)
            entropy -= p * log2(p)

        return round(entropy, 2)