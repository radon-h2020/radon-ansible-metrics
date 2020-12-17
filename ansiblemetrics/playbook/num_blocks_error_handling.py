from ansiblemetrics.ansible_metric import AnsibleMetric


class NumBlocksErrorHandling(AnsibleMetric):
    """ This class measures the number of times errors are handled within the blocks tasks.

    Blocks introduce the ability to handle errors in a way similar to exceptions in most programming languages.
    The tasks in the block would execute normally, if there is any error the rescue section would get executed with
    whatever you need to do to recover from the previous error.
    The always section runs no matter what previous error did or did not occur in the block and rescue sections.

    """

    def count(self):
        """Return the number of blocks error handling.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_blocks_error_handling import NumBlocksErrorHandling

            playbook = '''
            - name: Attempt and graceful roll back demo
              block:    # This block handle errors with rescue and always
                - debug:
                    msg: 'I execute normally'
                - name: i force a failure
                  command: /bin/false
                - debug:
                    msg: 'I never execute, due to the above task failing, :-('
              rescue:
                - debug:
                    msg: 'I caught an error'
                - name: i force a failure in middle of recovery! >:-)
                  command: /bin/false
                - debug:
                    msg: 'I also never execute :-('
              always:
                - debug:
                    msg: "This always executes"

            - name: A task with a block that does not handle errors
              block:    # This block does not
                - debug:
                    msg: 'I execute normally'
                - name: i force a failure
                  command: /bin/false
                - debug:
                    msg: 'I never execute, due to the above task failing, :-('
            '''

            NumBlocksErrorHandling(playbook).count()

            >> 1

        Returns
        -------
        int
            number of times blocks are used to handle errors

        """
        handled = 0

        for task in self.tasks:
            if task and 'block' in task and ('rescue' in task or 'always' in task):
                handled += 1

        return handled
