# Number of regex

It counts the number of times a regular expression is used to perform some operations, by looking at the ```regexp``` syntax in the script.

---

## Example
The following example contains **one** ```regexp```


``` yaml
---
- name: Remove Password
  lineinfile:
    path: "/opt/appdata/nzbget/nzbget.conf" # 3rd path
    regexp: ControlPassword=tegbzn6789
    line: 'ControlPassword='
    state: present
  when: nzbget_conf.stat.exists == False
```


---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```regexp``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_regex import NumRegex

str = '- name: Remove Password\n\tlineinfile:\n\t\tpath: "/opt/appdata/nzbget/nzbget.conf" # 3rd path\n\t\tregexp: ControlPassword=tegbzn6789\n\t\tline: \'ControlPassword=\'\n\t\tstate: present\n\twhen: nzbget_conf.stat.exists == False' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumRegex(script).count()
print('Number of regexp: ', count)

>>> Number of regexp: 1
```
