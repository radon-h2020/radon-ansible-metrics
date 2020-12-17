from ansiblemetrics.ansible_metric import AnsibleMetric


class NumAuthorizedKey(AnsibleMetric):
    """ This class measures the number of times a SSH key is set and/or updated in a playbook.

    The authorized_key property is used to add or remove SSH authorized keys for particular user accounts.
    """

    def count(self):
        """Return the occurrences of the authorized_key keyword.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_authorized_key import NumAuthorizedKey

            playbook = '''
            ---
            - name: Set authorized key taken from file
              authorized_key:
                user: charlie
                state: present
                key: "{{ lookup('file', '/home/charlie/.ssh/id_rsa.pub') }}"
            '''

            NumAuthorizedKey(playbook).count()

            >> 1

        Returns
        -------
        int
            authorized_key occurrences

        """

        return sum(1 for task in self.playbook if task and 'authorized_key' in task)
