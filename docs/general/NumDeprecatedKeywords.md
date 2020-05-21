# Number of deprecated keywords

It measures the number of [**deprecated keywords**](https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html) in an Ansible script.

---


## Example
The following example has one depecrated keyword that occurs twice, namely ```args```:

``` yaml
---
- hosts: localhost
  tasks:
  
  - name: Hello, Ansible!
    action: rust_helloworld
    args:                           # 1st deprecated keyword
      name: Ansible
    register: hello_ansible
  
  - name: Async Hello, Ansible!
    action: rust_helloworld
    args:                           # 2nd deprecated keyword
      name: Ansible
    async: 10
    poll: 1
    register: async_hello_ansible

```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsinged int```   |The number of deprecated keywords  |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.num_deprecated_keywords import NumDeprecatedKeywords

str = '---\n- hosts: localhost\n\ttasks:\n\t\n\t- name: Hello, Ansible!\n\t\taction: rust_helloworld\n\t\targs:\t\t\t\t\t\t\t\t\t\t\t\t\t # 1st deprecated keyword\n\t\t\tname: Ansible\n\t\tregister: hello_ansible\n\t\n\t- name: Async Hello, Ansible!\n\t\taction: rust_helloworld\n\t\targs:\t\t\t\t\t\t\t\t\t\t\t\t\t # 2nd deprecated keyword\n\t\t\tname: Ansible\n\t\tasync: 10\n\t\tpoll: 1\n\t\tregister: async_hello_ansible\n' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumDeprecatedKeywords(script).count()
print('Number of deprecated keywords: ', count)

>>> Number of deprecated keywords: 2
```