from ansiblemetrics.ansible_metric import AnsibleMetric


class NumBlocks(AnsibleMetric):
    """ This class measures the number of block sections in a playbook.

    Blocks allow for logical grouping of tasks and in play error handling.
    Most of what you can apply to a single task (with the exception of loops) can be applied at the block level, which
    also makes it much easier to set data or directives common to the tasks. This does not mean the directive affects
    the block itself, but is inherited by the tasks enclosed by a block, i.e. a when will be applied to the tasks,
    not the block itself.

    """

    def count(self):
        """Return the number of block sections.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_blocks import NumBlocks

            playbook = '''
            ---
            - name: Install, configure, and start Apache
              block:
              - name: install httpd and memcached
                yum:
                  name: "{{ item }}"
                  state: present
                loop:
                  - httpd
                  - memcached
              - name: start service bar and enable it
                service:
                  name: bar
                  state: started
                  enabled: True
              when: ansible_facts["distribution"] == "CentOS"
            '''

            NumBlocks(playbook).count()

            >> 1

        Returns
        -------
        int
            block occurrences

        """
        blocks = 0

        for task in self.playbook:
            if task and 'block' in task:
                blocks += 1

        return blocks
