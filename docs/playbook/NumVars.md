# Number of variables

It measures the number of [playbooks variables](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html) in the script.

**Note:** role and task variables are included, as well as [registered variables](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#registering-variables).
A major use of variables is running a command and registering the result of that command as a variable. When someone executes a task and save the return value in a variable for use in later tasks, s/he creates a registered variable.

---

## Example
The following example has three variables, namely ```http_port```, ```app_path``` and ```favcolor```:

``` yaml
---
- hosts: webservers
  vars:
    http_port: 80                       # 1st variable
    
- hosts: app_servers
  vars:
    app_path: "{{ base_path }}/22"      # 2nd variable

- hosts: all
  remote_user: root
  vars:
    favcolor: blue                      # 3rd variable
  vars_files:                           # !!! vars_files is not supported by this version
    - /vars/external_vars.yml
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of variables |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_vars import NumVars

str = '---\n- hosts: webservers\n\tvars:\n\t\thttp_port: 80\n\t\t\n- hosts: app_servers\n\tvars:\n\t\tapp_path: "{{ base_path }}/22"\n\n- hosts: all\n\tremote_user: root\n\tvars:\n\t\tfavcolor: blue\n\tvars_files:\n\t\t- /vars/external_vars.yml' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumVars(script).count()
print('Number of variables: ', count)

>>> Number of variables: 3
```