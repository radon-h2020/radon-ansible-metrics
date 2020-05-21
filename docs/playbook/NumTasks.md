# Number of tasks

It measures the number of [tasks](https://docs.ansible.com/ansible/2.4/playbooks_intro.html#basics) in the script.

---

## Example
The following script extracted from the [ansible-examples repository](https://github.com/ansible/ansible-examples/blob/master/phillips_hue/on_off.yml) 
has three tasks, namely ```INCLUDE UNIQUE USERNAME FROM REGISTER.YML```, ```GRAB HUE LIGHT INFORMATION``` and ```PRINT DATA TO TERMINAL WINDOW```.

``` yaml
- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML   # 1st task
  include_vars:                                     
    file: username_info.yml

- name: GRAB HUE LIGHT INFORMATION                  # 2nd task
  uri:                                              
    url: "http://{{ip_address}}/api/{{username}}"
    method: GET
    body: '{{body_info|to_json}}'
  register: light_info

- name: PRINT DATA TO TERMINAL WINDOW               # 3rd task
  debug:                                            
    var: light_info.json.lights
```


---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of tasks |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_tasks import NumTasks

str = '- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML\n\tinclude_vars:\n\t\tfile: username_info.yml\n\n- name: GRAB HUE LIGHT INFORMATION\n\turi:\n\t\turl: "http://{{ip_address}}/api/{{username}}"\n\t\tmethod: GET\n\t\tbody: "{{body_info|to_json}}"\n\tregister: light_info\n\n- name: PRINT DATA TO TERMINAL WINDOW\n\tdebug:\n\t\tvar: light_info.json.lights' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumTasks(script).count()
print('Number of tasks: ', count)

>>> Number of tasks: 3
```
