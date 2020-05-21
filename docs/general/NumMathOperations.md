# Number of math operations

It measures the number of math opeartions in an Ansible script.
The following operators are considered for the calculation: ```+, -, /, //, %, \*, \*\*```

---


## Example
The following script extracted from [mydailytutorials](http://www.mydailytutorials.com/ansible-arithmetic-operations/)
has **five** math operands

``` yaml
- hosts: localhost
  tasks:
  - debug:
      msg: "addition{{ 4 + 3 }}"          # 1st operation
  - debug:
      msg: "substraction {{ 4 - 3 }}"     # 2nd operation
  - debug:
      msg: "multiplication {{ 4 * 3 }}"   # 3rd operation
  - debug:
      msg: "Modulo operation {{ 7 % 4}}"  # 4th operation
  - debug:
      msg: "floating division {{ 4 / 3}}" # 5th operation
```
---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of arithmetic operations |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.num_math_operations import NumMathOperations

str = '- hosts: localhost\n\ttasks:\n\t- debug:\n\t\t\tmsg: "addition{{ 4 + 3 }}"\n\t- debug:\n\t\t\tmsg: "substraction {{ 4 - 3 }}"\n\t- debug:\n\t\t\tmsg: "multiplication {{ 4 * 3 }}"\n\t- debug:\n\t\t\tmsg: "Modulo operation {{ 7 % 4}}"\n\t- debug:\n\t\t\tmsg: "floating division {{ 4 / 3}}"' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumMathOperations(script).count()
print('Number of math operations: ', count)

>>> Number of math operations: 5
```