
# Number of roles

It measures the number of **distinct** [```roles```](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#playbooks-reuse-roles) in the script.

---

## Example
The following example from the [Ansible's documentation](https://docs.ansible.com/ansible/latest/user_guide/guide_rolling_upgrade.html?highlight=playbook) is a site-wide deployment playbook with six roles, namely ```common```, ```db```, ```base-apache```, ```web```, ```haproxy```, and ```nagios```:

``` yaml
---
- hosts: all            
  roles:
  - common              # 1st role

- hosts: dbservers
  roles:
  - db                  # 2nd role

- hosts: webservers  
  roles:
  - base-apache         # 3rd role
  - web                 # 4th role

- hosts: lbservers     
  roles:
  - haproxy             # 5th role

- hosts: monitoring     
  roles:
  - base-apache
  - nagios              # 6th role
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of roles |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_roles import NumRoles

str = '---\n- hosts: all\n\troles:\n\t- common\n\n- hosts: dbservers\n\troles:\n\t- db\n\n- hosts: webservers\n\troles:\n\t- base-apache\n\t- web\n\n- hosts: lbservers\n\troles:\n\t- haproxy\n\n- hosts: monitoring\n\troles:\n\t- base-apache\n\t- nagios' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumRoles(script).count()
print('Number of roles: ', count)

>>> Number of roles: 6
```
