from ansiblemetrics.ansible_metric import AnsibleMetric
from ansiblemetrics.ansible_modules import COMMANDS_MODULES


class NumCommands(AnsibleMetric):
    """ This class measures the occurrences of the following modules in a playbook:

    * command: execute commands on targets;
    * expect: executes a command and responds to prompts;
    * psexec: runs commands on a remote Windows host based on the PsExec model;
    * raw: executes a low-down and dirty command;
    * script: runs a local script on a remote node after transferring it;
    * shell: execute shell commands on targets;
    * telnet: executes a low-down and dirty telnet command.
    """

    def count(self):
        """Return the number of commands.

        Example
        -------
        .. highlight:: python
        .. code-block:: python

            from ansiblemetrics.general.num_commands import NumCommands

            playbook = '''
            ---
            - name: return motd to registered var
              command: cat /etc/motd
              register: mymotd

            - name: List user accounts on a Windows system
              raw: Get-WmiObject -Class Win32_UserAccount
            '''

            NumCommands(playbook).count()

            >> 2

        Returns
        -------
        int
            number of commands

        """

        commands = 0

        for task in self.tasks:
            if not task or type(task) != dict:
                continue

            if any(key in COMMANDS_MODULES for key in task.keys()):
                commands += 1

        return commands
