# Number of ```include_tasks```

It measures the number of [```include_tasks```](https://docs.ansible.com/ansible/latest/modules/include_tasks_module.html) statements in the script.

---

## Example
The following example has **two** ```include_tasks``` statements.
``` yaml
---
- name: Include task list in play
  include_tasks: stuff.yaml

- name: Apply tags to tasks within included file
  include_tasks:
    file: install.yml
    apply:
      tags:
        - install
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```include_tasks``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_include_tasks import NumIncludeTasks

str = '---\n- name: Include task list in play\n\tinclude_tasks: stuff.yaml\n\n- name: Apply tags to tasks within included file\n\tinclude_tasks:\n\t\tfile: install.yml\n\t\tapply:\n\t\t\ttags:\n\t\t\t\t- install' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumIncludeTasks(script).count()
print('Number of include_tasks: ', count)

>>> Number of include_tasks: 2
```