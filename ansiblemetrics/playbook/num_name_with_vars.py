import re

from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.utils import key_value_list


class NumNameWithVars(AnsibleMetric):
    """ This class measures the number of names that use variables.

    With uniqueness as a goal, many playbook authors look to variables to satisfy this constraint.
    This strategy may work well but authors need to take care as to the source of the variable data they are referencing.
    Variable data can come from a variety of locations, and the values assigned to variables can be defined at a variety
    of times. For the sake of play and task names, it is important to remember that only variables for which the values
    can be determined at playbook parse time will parse and render correctly. If the data of a referenced variable is
    discovered via a task or other operation, the variable string will be displayed unparsed in the output.

    """

    def count(self):
        """Return the number of plays and tasks with names referencing variables.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_name_with_vars import NumNameWithVars

            playbook = '''
            - name: play with a {{ var_name }}    # uses variable
              hosts: localhost
              vars:
                var_name: not-mastery

              tasks:
              - name: set a variable    # does not use variable
                set_fact:
                task_var_name: "defined variable"

            '''

            NumNameWithVars(playbook).count()

            >> 1

        Returns
        -------
        int
            number of plays and tasks with names referencing variables

        """
        names_with_vars = 0

        for k, v in key_value_list(self.playbook):
            if 'name' == k:
                if re.search(r'\{{2,2}\s*([\w\W]+)\s*\}{2,2}', str(v)) is not None:
                    names_with_vars += 1

        return names_with_vars
