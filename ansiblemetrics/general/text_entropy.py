from math import log2

import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class TextEntropy(AnsibleMetric):
    """ This class implements the metric 'Text Entropy' of an Ansible script. """

    def count(self):

        keys = utils.all_keys(self.playbook)
        values = utils.all_values(self.playbook)

        words = keys

        for v in values:
            words.extend(str(v).split())

        words_set = set(words)
        freq = {word: words.count(word) for word in words_set}

        entropy = 0
        for word in words_set:
            p = freq[word] / len(words)
            entropy -= p * log2(p)

        return round(entropy, 2)
