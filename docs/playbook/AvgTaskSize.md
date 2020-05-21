# Average task size

It measures the average size of a task in an Ansible playbook. 
The average size is the *number of executable lines of code of tasks* divided by the [number of tasks](./NumTasks.md)

**Note:** the average size is rounded off to the nearest unit.

---


## Example
The following example has 3 tasks, containing 3, 6, and 3 lines of code respectively. The average task size is measured as: ```round((3+6+3)/3) = 4```.

``` yaml
---
- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML   # 1st task
  include_vars:                                     
    file: username_info.yml

- name: GRAB HUE LIGHT INFORMATION                  # 2nd task
  uri:                                              
    url: "http://{{ip_address}}/api/{{username}}"
    method: GET
    body: '{{body_info|to_json}}'
  register: light_info

- name: PRINT DATA TO TERMINAL WINDOW               #3rd task
  debug:                                            
    var: light_info.json.lights
```
--

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The average play size rounded off to the nearest unit |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.avg_task_size import AvgTaskSize

str = '---\n- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML\n\tinclude_vars:\n\t\tfile: username_info.yml\n\n- name: GRAB HUE LIGHT INFORMATION\n\turi:\n\t\turl: "http://{{ip_address}}/api/{{username}}"\n\t\tmethod: GET\n\t\tbody: '{{body_info|to_json}}'\n\tregister: light_info\n\n- name: PRINT DATA TO TERMINAL WINDOW\n\tdebug:\n\t\tvar: light_info.json.lights' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = AvgTaskSize(script).count()
print('Average task size: ', count)

>>> Average task size: 4
```
