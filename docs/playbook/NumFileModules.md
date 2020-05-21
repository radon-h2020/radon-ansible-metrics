# Number of ```file``` modules

The [```file``` module](https://docs.ansible.com/ansible/latest/modules/file_module.html) manage files and file properties.

This property counts the number of ```file``` syntax occurrences.

---


## Example
The following example has **two** ```file``` occurrences.

``` yaml
- name: Change file ownership, group and permissions
  file:
    path: /etc/foo.conf
    owner: foo
    group: foo
    mode: '0644'

- name: Give insecure permissions to an existing file
  file:
    path: /work
    owner: root
    group: root
    mode: '1777'
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of occurrences of commands |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_file_modules import NumFileModules

str = '- name: Change file ownership, group and permissions\n\tfile:\n\t\tpath: /etc/foo.conf\n\t\towner: foo\n\t\tgroup: foo\n\t\tmode: \'0644\'\n\n- name: Give insecure permissions to an existing file\n\tfile:\n\t\tpath: /work\n\t\towner: root\n\t\tgroup: root\n\t\tmode: \'1777\''

script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumFileModules(script).count()
print('Number of file occurrences: ', count)

>>> Number of file occurrences: 2
```