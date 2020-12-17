from ansiblemetrics.utils import key_value_list

from ansiblemetrics.ansible_metric import AnsibleMetric


class NumPrompts(AnsibleMetric):
    """ This class measures the number of interactions with users by means of the module prompt. """

    def count(self):
        """Return the number of

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_prompts import NumPrompts

            playbook = '''
            - hosts: all
              remote_user: root

              vars_prompt:
                - name: "name"
                  prompt: "what is your name?"
                - name: "quest"
                  prompt: "what is your quest?"
                - name: "favcolor"
                  prompt: "what is your favorite color?"
            '''

            NumPrompts(playbook).count()

            >> 3

        Returns
        -------
        int
            number of

        """
        return sum(1 for k, v in key_value_list(self.playbook) if k == 'prompt')
