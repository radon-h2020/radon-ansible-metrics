# Number of keys

It measures the number of **keys** in the dictionary representing an Ansible script.

---

## Example
The following example has **nine** keys, namely 'hosts', 'roles', 'hosts', 'roles', 'tasks', 'name', 'mysql_db', 'name', 'state'.

``` yaml
- hosts: all
  roles:
  - common

# Configure and deploy database servers.
- hosts: dbservers
  roles:
  - db

tasks: 
  - name: Create Application Database
    mysql_db:
      name: "{{ dbname }}"
      state: present
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of keys in the dictionary  |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.num_keys import NumKeys

str = '- hosts: all\n\troles:\n\t- common\n\n# Configure and deploy database servers.\n- hosts: dbservers\n\troles:\n\t- db\n\ntasks: \n\t- name: Create Application Database\n\t\tmysql_db:\n\t\t\tname: "{{ dbname }}"\n\t\t\tstate: present' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumKeys(script).count()
print('Number of keys: ', count)

>>> Number of keys: 9
```