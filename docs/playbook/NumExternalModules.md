# Number of external modules

It measures the number of external modules in the script not belonging to the core Ansible or not maintained by the Ansible community.

---


## Example
The following example has 2 facts modules and three modules in total.

``` yaml
- name: ensure foo
  file:                       # Core module
    path: /tmp/foo
    state: touch

- name: do a remote copy
  remote_copy:                # External module
    source: /tmp/foo
    dest: /tmp/bar
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of external modules |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_external_modules import NumExternalModules

str = '- name: ensure foo\n\tfile:\n\t\tpath: /tmp/foo\n\t\tstate: touch\n\n- name: do a remote copy\n\tremote_copy:\n\t\tsource: /tmp/foo\n\t\tdest: /tmp/bar' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumExternalModules(script).count()
print('Number of external modules: ', count)

>>> Number of external modules: 1
```