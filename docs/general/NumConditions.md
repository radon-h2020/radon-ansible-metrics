# Number of conditions

It measures the number of **conditions** in an Ansible script.
A [*condition*](https://www.ibm.com/support/pages/what-difference-between-decision-and-condition) is a Boolean expression containing no Boolean operators.
Conditions are identified by the following comparison operators: ```is, in, ==, !=, >, >=, <, <=```

---


## Example
The following script extracted from [mydailytutorials](http://www.mydailytutorials.com/working-ansible-variables-conditionals/)
has **five** conditions

``` yaml
- hosts: all
  test1: "Hello World"
  tasks:
  - debug:
      msg: "Equals"
      when:
        - test1 == "Hello World"          # 1st condition
        - test1 != "Hello"                # 2nd condition
  - debug:
      msg: "Not Equals"
      when: test1 != "Hello World"        # 3rd condition
  - debug:
      msg: "Not Equals"
      when: test1 <= 5 or test1 >= 10     # 4th condition
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of conditions  |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.num_conditions import NumConditions

str = '- hosts: all\n\ttest1: "Hello World"\n\ttasks:\n\t- debug:\n\t\t\tmsg: "Equals"\n\t\t\twhen:\n\t\t\t\t- test1 == "Hello World"\t\t\t\t\t# 1st condition\n\t\t\t\t- test1 != "Hello"\t\t\t\t\t\t\t\t# 2nd condition\n\t- debug:\n\t\t\tmsg: "Not Equals"\n\t\t\twhen: test1 != "Hello World"\t\t\t\t# 3rd condition\n\t- debug:\n\t\t\tmsg: "Not Equals"\n\t\t\twhen: test1 <= 5 or test1 >= 10\t\t # 4th condition' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumConditions(script).count()
print('Number of conditions: ', count)

>>> Number of conditions: 5
```