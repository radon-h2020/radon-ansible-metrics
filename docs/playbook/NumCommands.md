# Number of ```commands```

Comments are non-executable parts of the script that are used for explanation.
This property counts the occurrences of the following modules in the script:

- [```command```](https://docs.ansible.com/ansible/latest/modules/command_module.html): Execute commands on targets;
- [```expect```](https://docs.ansible.com/ansible/latest/modules/expect_module.html): Executes a command and responds to prompts;
- [```psexec```](https://docs.ansible.com/ansible/latest/modules/psexec_module.html): Runs commands on a remote Windows host based on the PsExec model;
- [```raw```](https://docs.ansible.com/ansible/latest/modules/raw_module.html): Executes a low-down and dirty command;
- [```script```](https://docs.ansible.com/ansible/latest/modules/sript_module.html): Runs a local script on a remote node after transferring it;
- [```shell```](https://docs.ansible.com/ansible/latest/modules/shell_module.html): Execute shell commands on targets;
- [```telnet```](https://docs.ansible.com/ansible/latest/modules/telnet_module.html): Executes a low-down and dirty telnet command.

---


## Example
The following example has **eight** *commands* (the ```shell``` command occurs twice).

``` yaml
- name: return motd to registered var
  command: cat /etc/motd
  register: mymotd

- name: Case insensitive password string match
  expect:
    command: passwd username
    responses:
      (?i)password: "MySekretPa$$word"
  no_log: true

- name: Run a cmd.exe command
  psexec:
    hostname: server
    connection_username: username
    connection_password: password
    executable: cmd.exe
    arguments: /c echo Hello World

- name: List user accounts on a Windows system
  raw: Get-WmiObject -Class Win32_UserAccount

- name: Run a script with arguments (free form)
  script: /some/local/script.sh --some-argument 1234

- name: Execute the command in remote shell; stdout goes to the specified file on the remote.
  shell: somescript.sh >> somelog.txt

- name: Change the working directory to somedir/ before executing the command.
  shell: somescript.sh >> somelog.txt
  args:
    chdir: somedir/

- name: run show commands
  telnet:
    user: cisco
    password: cisco
    login_prompt: "Username: "
    prompts:
      - "[>#]"
    command:
      - terminal length 0
      - show version
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of occurrences of commands |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_commands import NumCommands

str = ''- name: return motd to registered var\n\tcommand: cat /etc/motd\n\tregister: mymotd\n\n- name: Case insensitive password string match\n\texpect:\n\t\tcommand: passwd username\n\t\tresponses:\n\t\t\t(?i)password: "MySekretPa$$word"\n\tno_log: true\n\n- name: Run a cmd.exe command\n\tpsexec:\n\t\thostname: server\n\t\tconnection_username: username\n\t\tconnection_password: password\n\t\texecutable: cmd.exe\n\t\targuments: /c echo Hello World\n\n- name: List user accounts on a Windows system\n\traw: Get-WmiObject -Class Win32_UserAccount\n\n- name: Run a script with arguments (free form)\n\tscript: /some/local/script.sh --some-argument 1234\n\n- name: Execute the command in remote shell; stdout goes to the specified file on the remote.\n\tshell: somescript.sh >> somelog.txt\n\n- name: Change the working directory to somedir/ before executing the command.\n\tshell: somescript.sh >> somelog.txt\n\targs:\n\t\tchdir: somedir/\n\n- name: run show commands\n\ttelnet:\n\t\tuser: cisco\n\t\tpassword: cisco\n\t\tlogin_prompt: "Username: "\n\t\tprompts:\n\t\t\t- "[>#]"\n\t\tcommand:\n\t\t\t- terminal length 0\n\t\t\t- show version'' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumCommands(script).count()
print('Number of commands occurrences: ', count)

>>> Number of commands occurrences: 8
```