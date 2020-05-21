# Number of unique ```name```

Given an Ansible script, the metric returns the number of unique names in play and tasks of the playbook.

The relative number of unique names is measured as the number of unique ```name``` divided by the total number of ```name``` in the script.
 
Naming plays and tasks uniquely is a best practice in general that will help to quickly identify where a problematic task may reside in your hierarchy of playbooks, roles, task files, handlers and so on. Uniqueness is more important when notifying a handler or when starting at a specific task. When task names have duplicates, the behavior of Ansible may be nondeterministic or at least not obvious.

The implementation of this metric assumes names with same string and variable as equal (even though the variable value can vary through the execution workflow).


---

## Example
The following example is a playbook contains three ```name```, one of which is unique: 

``` yaml
---
- name: demo the logic                    # unique name
  hosts: localhost
  gather_facts: false
  vars:
  num1: 10
  num3: 10
  tasks:
  - name: logic and comparison            # duplicate
    debug:
      msg: "Can you read me?"
    when: num1 >= num3 and num1 is even and num2 is not defined
  - name: logic and comparison            # duplicate
    debug:
      msg: "Can you read me again?"
    when: num3 >= num1    
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of unique ```name``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_unique_names import NumUniqueNames

str = '- name: demo the logic\n\thosts: localhost\n\tgather_facts: false\n\tvars:\n\tnum1: 10\n\tnum3: 10\n\ttasks:\n\t- name: logic and comparison\n\t\tdebug:\n\t\t\tmsg: "Can you read me?"\n\t\twhen: num1 >= num3 and num1 is even and num2 is not defined\n\t- name: logic and comparison\n\t\tdebug:\n\t\t\tmsg: "Can you read me again?"\n\t\twhen: num3 >= num1' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumUniqueNames(script).count()
print('Number of unique names: ', count)

>>> Number of unique names: 1
```