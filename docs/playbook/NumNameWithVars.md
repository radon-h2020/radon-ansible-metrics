# Number of ```name``` with variables

It measures the number of names that use variables.

With uniqueness as a goal, many playbook authors look to variables to satisfy this constraint. This strategy may work well but authors need to take care as to the source of the variable data they are referencing. Variable data can come from a variety of locations, and the values assigned to variables can be defined at a variety of times. For the sake of play and task names, it is important to remember that only variables for which the values can be determined at playbook parse time will parse and render correctly. If the data of a referenced variable is discovered via a task or other operation, the variable string will be displayed unparsed in the output.

---


## Example
The following example has *five names*, of which **four using variables**. 

``` yaml
---
- name: play with a {{ var_name }}                  # 1st name with variable
  hosts: localhost
  vars:
    var_name: not-mastery
  
  tasks:
  - name: set a variable
    set_fact:
    task_var_name: "defined variable"

  - name: task with a {{ task_var_name }}           # 2nd name with variable
    debug:
    msg: "I am mastery task"

- name: second play with a {{ task_var_name }}      # 3rd name with variable
  hosts: localhost

  tasks:
  - name: task with a {{ runtime_var_name }}        # 4th name with variable
    debug:
      msg: "I am another mastery task"
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```name``` with variables |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_name_with_variables import NumNameWithVariables

str = '- name: play with a {{ var_name }}\n\thosts: localhost\n\tvars:\n\t\tvar_name: not-mastery\n\t\n\ttasks:\n\t- name: set a variable\n\t\tset_fact:\n\t\ttask_var_name: "defined variable"\n\n\t- name: task with a {{ task_var_name }}\n\t\tdebug:\n\t\tmsg: "I am mastery task"\n\n- name: second play with a {{ task_var_name }}\n\thosts: localhost\n\n\ttasks:\n\t- name: task with a {{ runtime_var_name }}\n\t\tdebug:\n\t\t\tmsg: "I am another mastery task"' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumNameWithVariables(script).count()
print('Number of name with variables: ', count)

>>> Number of name with variables: 4
```
