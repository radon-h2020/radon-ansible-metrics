import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_keywords import DEPRECATED_KEYWORDS
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumDeprecatedKeywords(AnsibleMetric):
    """ This class measures the number of deprecated keywords in a playbook

    More info about Ansible deprecated keywords can be found at: https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html
    """

    def count(self):
        """Return the number of Ansible deprecated keywords.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_deprecated_keywords import NumDeprecatedKeywords

            playbook = '''
            - hosts: localhost

              tasks:
              - name: Hello, Ansible!
                action: rust_helloworld
                args:   # Deprecated keyword
                  name: Ansible
            '''

            NumDeprecatedKeywords(playbook).count()

            >> 1

        Returns
        -------
        int
            Number of deprecated keywords
        """
        deprecated = []

        keys = utils.all_keys(self.playbook)

        for k in keys:
            if k in DEPRECATED_KEYWORDS:
                deprecated.append(k)

        return len(deprecated)
