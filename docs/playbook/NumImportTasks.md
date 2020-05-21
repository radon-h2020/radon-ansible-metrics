# Number of ```import_tasks```

It measures the number of [```import_tasks```](https://docs.ansible.com/ansible/latest/modules/import_tasks_module.html) statements in the script.

---

## Example
The following example has **two** ```import_tasks``` statements.

``` yaml
- name: Include task list in play
  import_tasks: stuff.yaml

- name: Apply conditional to all imported tasks
  import_tasks: stuff.yaml
  when: hostvar is defined
```


---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```import_tasks``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_import_tasks import NumImportTasks

str = '- name: Include task list in play\n\timport_tasks: stuff.yaml\n\n- name: Apply conditional to all imported tasks\n\timport_tasks: stuff.yaml\n\twhen: hostvar is defined' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumImportTasks(script).count()
print('Number of import_tasks: ', count)

>>> Number of import_tasks: 2
```

