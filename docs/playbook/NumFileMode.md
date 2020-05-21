# Number of ```mode``` in file modules

File ```mode``` is a source code property used to manage files, directories and symblic links.

This property counts the number of ```mode``` syntax occurrences, used to set the permissions a file or a directory should have.

---


## Example
The following example has **two** ```mode``` occurrences.

``` yaml
- name: Change file ownership, group and permissions
  file:
    path: /etc/foo.conf
    owner: foo
    group: foo
    mode: '0644'    # 1st occurrence 

- name: Replace a localhost entry with our own
  lineinfile:
    path: /etc/hosts
    regexp: '^127\.0\.0\.1'
    line: 127.0.0.1 localhost
    owner: root
    group: root
    mode: '0644'    # 2nd occurrence
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of occurrences of file mode |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_file_mode import NumFileMode

str = '- name: Change file ownership, group and permissions\n\tfile:\n\t\tpath: /etc/foo.conf\n\t\towner: foo\n\t\tgroup: foo\n\t\tmode: \'0644\'\n\n- name: Replace a localhost entry with our own\n\tlineinfile:\n\t\tpath: /etc/hosts\n\t\tregexp: \'^127\.0\.0\.1\'\n\t\tline: 127.0.0.1 localhost\n\t\towner: root\n\t\tgroup: root\n\t\tmode: \'0644\''

script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumFileMode(script).count()
print('Number of file mode occurrences: ', count)

>>> Number of file mode occurrences: 2
```