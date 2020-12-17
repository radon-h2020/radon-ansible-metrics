import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumLoops(AnsibleMetric):
    """ This class measures the number of loops in a playbook. """

    def count(self):
        """Return the number of loops.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_loops import NumLoops

            playbook = '''
            ---
            - name: with_list
              debug:
                msg: "{{ item }}"
              with_list:    # 1st loop
                - one
                - two

            - name: with_list -> loop
              debug:
                msg: "{{ item }}"
              loop:    # 2nd loop
                - one
                - two
            '''

            NumLoops(playbook).count()

            >> 2

        Returns
        -------
        int
            number of loops

        """
        return sum(1 for key in utils.all_keys(self.playbook) if key == 'loop' or str(key).startswith('with_'))
