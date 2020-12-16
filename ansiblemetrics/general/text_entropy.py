from math import log2

import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class TextEntropy(AnsibleMetric):
    """ This class measure the Shannon entropy of a playbook's text.
    The entropy is computed considering the tokens as symbols, rather than the letters.
    """

    def count(self):
        """Return the playbook's text entropy.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.text_entropy import TextEntropy

            playbook = '''
            ---
            - hosts: all
              roles:
              - common

            - hosts: dbservers
              roles:
              - db
              - web
            '''

            TextEntropy(playbook).count()

            >> 4.89

        Returns
        -------
        float
            Text entropy
        """

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
