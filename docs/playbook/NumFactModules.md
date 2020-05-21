# Number of fact modules

It measures the number of facts modules in the script.

Fact modules are modules that do not alter state but rather return data. 
Knowing the number of fact modules in a playbook could represent a measure of the responsibility of the playbook. 
The assumption is that the lower the fact modules wrt the total number of modules in the script, the more unstable is the behaviour of the class, as the other modules alter its state.

---

## Example
The following example has 2 facts modules and three modules in total.

``` yaml
tasks:
  - name: Find all instances in the specified region    
    ali_instance_facts:                                   # 1st fact module
      alicloud_access_key: '{{ alicloud_access_key }}'
      alicloud_secret_key: '{{ alicloud_secret_key }}'
      alicloud_region: '{{ alicloud_region }}'
    register: all_instances

  - name: Find all instances based on the specified ids
    ali_instance_facts:                                   # 2nd fact module
      alicloud_access_key: '{{ alicloud_access_key }}'
      alicloud_secret_key: '{{ alicloud_secret_key }}'
      alicloud_region: '{{ alicloud_region }}'
    register: instances_by_ids

  - name: PRINT DATA TO TERMINAL WINDOW
    debug:                                                # not fact module
      msg: 'End of tasks'
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of fact modules |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_fact_modules import NumFactModules

str = 'tasks:\n\t- name: Find all instances in the specified region\t\t\n\t\tali_instance_facts:\n\t\t\talicloud_access_key: "{{ alicloud_access_key }}"\n\t\t\talicloud_secret_key: "{{ alicloud_secret_key }}"\n\t\t\talicloud_region: "{{ alicloud_region }}"\n\t\tregister: all_instances\n\n\t- name: Find all instances based on the specified ids\n\t\tali_instance_facts:\n\t\t\talicloud_access_key: "{{ alicloud_access_key }}"\n\t\t\talicloud_secret_key: "{{ alicloud_secret_key }}"\n\t\t\talicloud_region: "{{ alicloud_region }}"\n\t\tregister: instances_by_ids\n\n\t- name: PRINT DATA TO TERMINAL WINDOW\n\t\tdebug:\n\t\t\tmsg: "End of tasks"' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumFactModules(script).count()
print('Number of fact modules: ', count)

>>> Number of fact modules: 2
```