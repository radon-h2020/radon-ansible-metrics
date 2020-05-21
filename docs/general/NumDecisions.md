# Number of decisions

It measures the number of **decision** in an Ansible script.
A [*decision*](https://www.ibm.com/support/pages/what-difference-between-decision-and-condition) is a Boolean expression composed of conditions and one or more Boolean operators.
Conditions are identified by the following logical operators: ```and, or, not```.

**Note:** A decision without a Boolean operator is a condition.  

---


# Example
The following script extracted has **four** decisions

``` yaml
- hosts: all
  tasks:
  - debug:
      msg: "Equals"
      when: test1 == "Hello World" or test1 == "Hello"      # 1st decision
  - debug:
      msg: "Not Equals"
      when: 
        - test1 == "Hello World" and not test2 == test1     # 2nd (and) and 3rd (not) decision
        - test3 == "Waldo"                                  # 4th decision (multiple conditions that all need to be true (a logical ‘and’) can be specified as a list)
```
---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of decisions  |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.num_decisions import NumDecisions

str = '- hosts: all\n\ttasks:\n\t- debug:\n\t\t\tmsg: "Equals"\n\t\t\twhen: test1 == "Hello World" or test1 == "Hello"\n\t- debug:\n\t\t\tmsg: "Not Equals"\n\t\t\twhen: \n\t\t\t\t- test1 == "Hello World" and not test2 == test1\n\t\t\t\t- test3 == "Waldo"' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumDecisions(script).count()
print('Number of decisions: ', count)

>>> Number of decisions: 4
```