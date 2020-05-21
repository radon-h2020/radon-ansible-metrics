# Lines of code

It measures the number of **executable** lines of code.

---

## Example
The following example has **8 executable lines of code**. Blank and commented lines are not considered _executable_ lines of code.

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

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of executable lines of code  |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.lines_code import LinesCode

str = '---\n- hosts: localhost\n\n\ttasks:\n\t- name: task 1\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml\n\n\t- name: task 2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = LinesCode(script).count()
print('Lines of code: ', count)

>>> Lines of code: 8
```