# Number of ```block```'s

It returns the number of [```block```](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html) in the script.
Blocks allow for logical grouping of tasks and in play error handling. Most of what you can apply to a single task (with the exception of loops) can be applied at the block level, which also makes it much easier to set data or directives common to the tasks. This does not mean the directive affects the block itself, but is inherited by the tasks enclosed by a block, i.e. a when will be applied to the tasks, not the block itself.

---

## Example
The following example from the [Ansible's documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html) repository has only one block:

``` yaml
- name: Install, configure, and start Apache
  block:         
  - name: install httpd and memcached
    yum:
      name: "{{ item }}"
      state: present
    loop:
      - httpd
      - memcached
  - name: start service bar and enable it
    service:
      name: bar
      state: started
      enabled: True
  when: ansible_facts["distribution"] == "CentOS"
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of blocks |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_blocks import NumBlocks

str = '- name: Install, configure, and start Apache\n\tblock:\t\t\t\t \n\t- name: install httpd and memcached\n\t\tyum:\n\t\t\tname: "{{ item }}"\n\t\t\tstate: present\n\t\tloop:\n\t\t\t- httpd\n\t\t\t- memcached\n\t- name: start service bar and enable it\n\t\tservice:\n\t\t\tname: bar\n\t\t\tstate: started\n\t\t\tenabled: True\n\twhen: ansible_facts["distribution"] == "CentOS"' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumBlocks(script).count()
print('Number of blocks: ', count)

>>> Number of blocks: 1
```
