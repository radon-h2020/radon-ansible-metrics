# Number of plays

It measures the number of [plays](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html) in the script.

---


## Example
The following example from the [Ansible's documentation](https://docs.ansible.com/ansible/latest/user_guide/guide_rolling_upgrade.html?highlight=playbook) is a site-wide deployment playbook with five plays, targeting the ```dbserver```, the ```webserver```, the ```lbserver```, and the ```monitoring```, respectively:


``` yaml
---
- hosts: all            # 1st play
  roles:
  - common

- hosts: dbservers      # 2nd play
  roles:
  - db

- hosts: webservers     # 3rd play
  roles:
  - base-apache
  - web

- hosts: lbservers      # 4th play
  roles:
  - haproxy

- hosts: monitoring     # 5th play
  roles:
  - base-apache
  - nagios
```


---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of plays |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_plays import NumPlays

str = '---\n- hosts: all\n\troles:\n\t- common\n\n- hosts: dbservers\n\troles:\n\t- db\n\n- hosts: webservers\n\troles:\n\t- base-apache\n\t- web\n\n- hosts: lbservers\n\troles:\n\t- haproxy\n\n- hosts: monitoring\n\troles:\n\t- base-apache\n\t- nagios' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumPlays(script).count()
print('Number of plays: ', count)

>>> Number of plays: 5
```
