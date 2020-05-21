# Number of loops

It measures the number of [loops](https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html) in the script.

---

## Example
The following example has two loops indicated by the keywords ```loop``` and ```with_*```

``` yaml
---
- name: with_list
  debug:
    msg: "{{ item }}"
  with_list:            # 1st loop
    - one
    - two

- name: with_list -> loop
  debug:
    msg: "{{ item }}"
  loop:                 # 2nd loop
    - one
    - two
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of loops |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_loops import NumLoops

str = '- name: with_list\n\tdebug:\n\t\tmsg: "{{ item }}"\n\twith_list:\n\t\t- one\n\t\t- two\n\n- name: with_list -> loop\n\tdebug:\n\t\tmsg: "{{ item }}"\n\tloop:\n\t\t- one\n\t\t- two' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumLoops(script).count()
print('Number of loops: ', count)

>>> Number of loops: 2
```
