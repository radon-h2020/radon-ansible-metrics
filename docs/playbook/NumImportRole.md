# Number of ```import_role```

It measures the number of [import_role](https://docs.ansible.com/ansible/latest/modules/import_role_module.html) statements in the script.

---

## Example
The following example has **two** ```import_role``` statements.

``` yaml
- import_role:
    name: myrole

- name: Run tasks/other.yaml instead of "main"
  import_role:
    name: myrole
    tasks_from: other
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```import_role``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_import_role import NumImportRole

str = '- import_role:\n\t\tname: myrole\n\n- name: Run tasks/other.yaml instead of "main"\n\timport_role:\n\t\tname: myrole\n\t\ttasks_from: other' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumImportRole(script).count()
print('Number of import_role: ', count)

>>> Number of import_role: 2
```
