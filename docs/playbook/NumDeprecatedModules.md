# Number of deprecated modules

It measures the number of times tasks call **deprecated** [Ansible modules](https://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html).


---


## Example
The following example is a playbook containing one depecrated module, occurring twice, namely ```oc```:

``` yaml
- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML
  include_vars:                           # non deprecated module
    file: username_info.yml

- name: Create a service
  oc:                                     # deprecated module
    state: present
    name: myservice
    namespace: mynamespace
    kind: Service

- name: Delete a service
  oc:                                     # deprecated module
    state: absent
    name: myservice
    namespace: mynamespace
    kind: Service
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of deprecated modules |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_deprecated_modules import NumDeprecatedModules

str = '- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML\n\tinclude_vars:\n\t\tfile: username_info.yml\n\n- name: Create a service\n\toc:\n\t\tstate: present\n\t\tname: myservice\n\t\tnamespace: mynamespace\n\t\tkind: Service\n\n- name: Delete a service\n\toc:\n\t\tstate: absent\n\t\tname: myservice\n\t\tnamespace: mynamespace\n\t\tkind: Service' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumDeprecatedModules(script).count()
print('Number of deprecated modules: ', count)

>>> Number of deprecated modules: 2
```