# Number of filters

It measures the number of [filters](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html) in the script.

---

## Example
The following example from the [Ansible's documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html) has two filters, namely ```from_yaml_all``` and ```list```:

``` yaml
tasks:
  - shell: cat /some/path/to/multidoc-file.yaml
    register: result
  - debug:
      msg: '{{ item }}'
    loop: '{{ result.stdout | from_yaml_all | list }}'  # 2 filters 
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of filters |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_filters import NumFilters

str = 'tasks:\n\t- shell: cat /some/path/to/multidoc-file.yaml\n\t\tregister: result\n\t- debug:\n\t\t\tmsg: '{{ item }}'\n\t\tloop: "{{ result.stdout | from_yaml_all | list }}"' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumFilters(script).count()
print('Number of filters: ', count)

>>> Number of filters: 2
```