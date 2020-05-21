# Average play size

It measures the average size of a play in an Ansible playbook. 
The average size is the [number of executable lines of code](../general/LinesCode.md) divided by the [number of plays](./NumPlays.md)

**Note:** the average size is rounded off to the nearest unit.


---

## Example
The following example has 5 plays for a total of 17 executable lines of code. 
The average play size is: ```round(17/5) = round(3.4) = 3```.

``` yaml
---
- hosts: all
  roles:
  - common

- hosts: dbservers
  roles:
  - db

- hosts: webservers
  roles:
  - base-apache
  - web

- hosts: lbservers
  roles:
  - haproxy

- hosts: monitoring
  roles:
  - base-apache
  - nagios
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The average play size rounded off to the nearest unit |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.avg_play_size import AvgPlaySize

str = '---\n- hosts: all\n\troles:\n\t- common\n\n- hosts: dbservers\n\troles:\n\t- db\n\n- hosts: webservers\n\troles:\n\t- base-apache\n\t- web\n\n- hosts: lbservers\n\troles:\n\t- haproxy\n\n- hosts: monitoring\n\troles:\n\t- base-apache\n\t- nagios' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = AvgPlaySize(script).count()
print('Average play size: ', count)

>>> Average play size: 3
```