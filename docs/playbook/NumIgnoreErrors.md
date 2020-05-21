# Number of ```ignore_errors```

It measures the number of [```ignore_errors```](https://docs.ansible.com/ansible/latest/user_guide/playbooks_error_handling.html) in the script.

Ignoring errors is considered as a bad practice, since ignore errors only obscures error handling; there are better ways for [handling errors](https://blog.newrelic.com/engineering/ansible-best-practices-guide/).

---

## Example
The following example from the [Ansible's documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_error_handling.html#ignoring-failed-commands) repository has one ```ignore_errors``` (but it could be at least one per task):

``` yaml
- name: this will not be counted as a failure
  command: /bin/false
  ignore_errors: yes
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```ignore_errors: yes``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_ignore_errors import NumIgnoreErrors

str = '- name: this will not be counted as a failure\n\tcommand: /bin/false\n\tignore_errors: yes' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumIgnoreErrors(script).count()
print('Number of ignore_errors: ', count)

>>> Number of ignore_errors: 1
```
