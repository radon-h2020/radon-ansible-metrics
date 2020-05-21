# Number of ```include_vars```

It measures the number of [```include_vars```](https://docs.ansible.com/ansible/latest/modules/include_vars_module.html?highlight=include_vars) statements in the script.

---

## Example
The following example has **one** ```include_vars``` statement.


``` yaml
---
- name: Include a play after another play
  include_vars: myvars.yaml

- name: Include task list in play
  include_role: role.yaml
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```include_vars``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_include_vars import NumIncludeVars

str = '- name: Include a play after another play\n\tinclude_vars: myvars.yaml\n\n- name: Include task list in play\n\tinclude_role: role.yaml' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumIncludeVars(script).count()
print('Number of include_vars: ', count)

>>> Number of include_vars: 1
```