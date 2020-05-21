# Number of ```import_playbook```

It measures the number of [```import_playbook```](https://docs.ansible.com/ansible/latest/modules/import_playbook_module.html) statements in the script.

---


## Example
The following example has **two** ```import_playbook``` statements.

``` yaml
- name: Include a play after another play
  import_playbook: otherplays.yaml

- name: This fails because I'm inside a play already
  import_playbook: stuff.yaml
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```import_playbook``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_import_playbook import NumImportPlaybook

str = '- name: Include a play after another play\n\timport_playbook: otherplays.yaml\n\n- name: This fails because I am inside a play already\n\timport_playbook: stuff.yaml' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumImportPlaybook(script).count()
print('Number of import_playbook: ', count)

>>> Number of import_playbook: 2
```
