# Number of distinct modules

It measures the number of distinct [Ansible modules](https://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html) in the script.

This metric differs from [NumTasks](./NumTasks.md) as it counts for the number of distinct modules in the script, without duplicates. If a module occurs twice or more among tasks it is counted only once. Remember that the goal of a _task_ is to execute a module, so the total number of modules (with duplicates) equals the number of tasks.

---


## Example
The following example from the [ansible-examples](https://github.com/ansible/ansible-examples/blob/master/phillips_hue/on_off.yml) 
repository has three distinct modules, namely: ```include_vars```, ```uri``` and ```debug```:

``` yaml
- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML
  include_vars:                                     # 1st distinct module
    file: username_info.yml

- name: GRAB HUE LIGHT INFORMATION
  uri:                                              # 2nd distinct module
    url: "http://{{ip_address}}/api/{{username}}"
    method: GET
    body: '{{body_info|to_json}}'
  register: light_info

- name: PRINT DATA TO TERMINAL WINDOW
  debug:                                            # 3rd distinct module
    var: light_info.json.lights
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of distinct modules |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_distinct_modules import NumDistinctModules

str = '- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML\n\tinclude_vars:\n\t\tfile: username_info.yml\n\n- name: GRAB HUE LIGHT INFORMATION\n\turi:\n\t\turl: "http://{{ip_address}}/api/{{username}}"\n\t\tmethod: GET\n\t\tbody: "{{body_info|to_json}}"\n\tregister: light_info\n\n- name: PRINT DATA TO TERMINAL WINDOW\n\tdebug:\n\t\tvar: light_info.json.lights' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumDistinctModules(script).count()
print('Number of distinct modules: ', count)

>>> Number of distinct modules: 3
```