# Number of source lines of code (LOC)

Given a yaml file, the metric returns the number of _source_ lines of code.

**_Input_:**
* _yaml_ : StringIO -- a StringIO object representing a yaml file;

**_Output_:** an _integer >= 0_.

**_Exception_:** _YAMLError_ if the value of _yaml_ does not represent a valid yaml file.

#### Example
The following example has **8 source lines of code**. Blank and commented lines do not count as _source lines of code_.

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

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from ansiblemetrics.general.loc import LOC

>>> str = 'tasks:\n\t- name: Find all instances in the specified region\n\t\tali_instance_facts ...' 
>>> yml = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
>>> metric = LOC(yml)
>>> print('LOC: ' + str(metric.count()))

LOC: 8
```