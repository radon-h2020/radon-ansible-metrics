# Lines of comment

It measures the number of **commented** lines of code.

---

## Example

The following example has **2 commented lines of code**. 

``` yaml
---
- hosts: localhost

  tasks:
  # Defining the first task
  - name: task 1
    include_vars:
      file: username_info.yml

  # Defining the second task
  - name: task 2
    include_vars:
      file: username_info.yml
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of commented lines  |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.lines_comment import LinesComment

str = '---\n- hosts: localhost\n\n\ttasks:\n\t# Defining the first task\n\t- name: task 1\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml\n\n\t# Defining the second task\n\t- name: task 2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = LinesComment(script).count()
print('Lines of comment: ', count)

>>> Lines of comment: 2
```