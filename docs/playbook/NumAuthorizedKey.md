# Number of ```authorized_key```

This property counts the number of [```authorized_key```](https://docs.ansible.com/ansible/latest/modules/authorized_key_module.html)  syntax occurrences, used to adds or removes SSH authorized keys for particular user accounts.
---


## Example
The following example has **one** ```authorized_key``` occurrence.

``` yaml
- name: Set authorized key taken from file
  authorized_key:
    user: charlie
    state: present
    key: "{{ lookup('file', '/home/charlie/.ssh/id_rsa.pub') }}"
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of occurrences of ```authorized_key``` syntax |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_authorized_key import NumAuthorizedKey

str = '- name: Set authorized key taken from file\n\tauthorized_key:\n\t\tuser: charlie\n\t\tstate: present\n\t\tkey: "{{ lookup(\'file\', \'/home/charlie/.ssh/id_rsa.pub\') }}"'

script = NumAuthorizedKey(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumFileMode(script).count()
print('Number of authorized_key occurrences: ', count)

>>> Number of authorized_key occurrences: 1
```