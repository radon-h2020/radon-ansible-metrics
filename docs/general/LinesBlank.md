# Lines blank

It measures the number of **blank** lines of code.

---

## Example
The following example has **2 blank lines of code**.

``` yaml
---
- hosts: localhost

  tasks:
  - name: task 1
    include_vars:
      file: username_info.yml

  - name: task 2
    include_vars:
      file: username_info.yml
```

---

## Parameters

|                |Type                  |Description |
|----------------|----------------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of blank lines  |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.lines_blank import LinesBlank

str = '- hosts: localhost\n\n\ttasks:\n\t- name: task 1\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml\n\n\t- name: task 2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = LinesBlank(script).count()
print('Lines blank: ', count)

>>> Lines blank: 2
```