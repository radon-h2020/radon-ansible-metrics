# Number of ```include```

It measures the number of [```include```](https://docs.ansible.com/ansible/latest/modules/include_module.html) statements in the script.

---

## Example
The following example has **one** ```include``` statement.


``` yaml
---
- name: Include a play after another play
  include: otherplays.yaml

- name: Include task list in play
  include_role: role.yaml 
```


---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```include``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_include import NumInclude

str = '---\n- name: Include a play after another play\n\tinclude: otherplays.yaml\n\n- name: Include task list in play\n\tinclude_role: role.yaml' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumInclude(script).count()
print('Number of include: ', count)

>>> Number of include: 1
```