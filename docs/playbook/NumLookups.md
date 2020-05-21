# Number of lookups

It measures the number of times it [accesses data from outside source](https://ansible-manual.readthedocs.io/en/latest/playbooks_lookups.html).

Lookups are evaluated when the task referencing them is executed, which allows for dynamic data discovery. To reuse a particular lookup in multiple tasks and re-evaluate it each time, a playbook variable can be defined with a lookup value. Each time the playbook variable is referenced the lookup will be executed, potentially providing different values over time.

---


## Example
The following example from the [Ansible's documentation](https://ansible-manual.readthedocs.io/en/latest/playbooks_lookups.html) has one ```lookup```:

``` yaml
- hosts: all
  vars:
    contents: "{{ lookup('file', '/etc/foo.txt') }}"       # lookup
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of lookups |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_lookups import NumLookups

str = '- hosts: all\n\tvars:\n\t\tcontents: "{{ lookup('file', '/etc/foo.txt') }}"' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumLookups(script).count()
print('Number of lookups: ', count)

>>> Number of lookups: 1
```