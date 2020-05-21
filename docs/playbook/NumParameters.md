# Number of parameters

Modules in Ansible have paramaters that describe the desired state of the module; each parameter handles some aspect of the module. For example, the module ```file``` has a ```mode``` parameter that specifies the permissions for the file.

This property counts the number of parameters in an Ansible script.

---


## Example
The following example has **three** parameters.

``` yaml
- name: Create two hard links
  file:
    src: '/tmp/{{ item.src }}'  # 1st parameter
    dest: '{{ item.dest }}'     # 2nd parameter
    state: hard                 # 3rd parameter
  loop:
    - { src: x, dest: y }
    - { src: z, dest: k }

```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of parameters |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_parameters import NumParameters

str = '- name: Create two hard links\n\tfile:\n\t\tsrc: \'/tmp/{{ item.src }}\'\n\t\tdest: \'{{ item.dest }}\'\n\t\tstate: hard\n\tloop:\n\t\t- { src: x, dest: y }\n\t\t- { src: z, dest: k }'

script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumParameters(script).count()
print('Number of modules\' parameters: ', count)

>>> Number of file modules' parameters: 3
```