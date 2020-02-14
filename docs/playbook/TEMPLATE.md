# Average play size (APLS)

## Description 

Given an Ansible script, the metric returns the average size of a play in the script.

---

## Parameters

**_Input:_** 
* ```script : StringIO``` -- a StringIO object representing a IaC script in Ansible;

**_Output:_** 
* an *integer >= 0*. If the result is a floating number, it is rounded to the nearest unit.
 
**_Exception_:** 
* ```NotStringIOError``` if parameter ```script``` is not an instance of StringIO;
* ```NotPlaybookError``` if parameter ```script``` does not represent a valid Ansible script.

---

## Example
The following example has 5 plays, three having 3 loc and two having 4 loc. The average task size is measured as: ```round((3+3+4+3+4)/5) = round(3.4) = 3```.

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

Below an example on how to call the metric and the expected output for the aforementioned example:

```python
>>> from io import StringIO
>>> from ansiblemetrics.playbook.apls import APLS

>>> str = 'TODO' 
>>> script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
>>> metric = APLS(yml)
>>> print('Average play size: ' + str(metric.count()))

Average play size: 3
```