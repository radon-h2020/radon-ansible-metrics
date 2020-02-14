# Number of commented lines of code (CLOC)

Given a yaml file, the metric returns the number of _commented_ lines of code.

**_Input:_** 
* ```script : StringIO``` -- a StringIO object representing a IaC script in Ansible;
* ```relative : boolean```  -- a boolean value indicating whether to return the absolute or relative number of blocks error handling. Default is _False_ (meaning to return the absolute value).

**_Output:_** 
* a *floating number >= 0 *.

**_Exception_:** _YAMLError_ if the value of _yaml_ does not represent a valid yaml file.

#### Example
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

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from ansiblemetrics.general.cloc import CLOC

>>> str = 'tasks:\n\t- name: Find all instances in the specified region\n\t\tali_instance_facts ...' 
>>> yml = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
>>> metric = CLOC(yml)
>>> print('CLOC: ' + str(metric.count()))

CLOC: 2
```