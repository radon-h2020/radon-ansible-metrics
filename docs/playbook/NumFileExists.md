# Number of check for file/dir existence

The module ```stat``` retrieves facts for a file similar to the Linux/Unix ‘stat’ command, and can be used to check for the existence of a file or directory. 

This property counts the number of ```*.(win_)?stat.* is (not)? defined``` syntax occurrences, to check if the file or directory exist.

---


## Example
The following example has **two** ```mode``` occurrences.

``` yaml
# Determine if a path exists and is a symlink. Note that if the path does
# not exist, and we test sym.stat.islnk, it will fail with an error. So
# therefore, we must test whether it is defined.
# Run this to understand the structure, the skipped ones do not pass the
# check performed by 'when'
- stat:
    path: /path/to/something
  register: sym

- debug:
    msg: "islnk isn't defined (path doesn't exist)"
  when: sym.stat.islnk is not defined  # file check

```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of checks for file existence |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_file_exists import NumFileExists

str = '- stat:\n\t\tpath: /path/to/something\n\tregister: sym\n\n- debug:\n\t\tmsg: "islnk is not defined (path does not exist)"\n\twhen: sym.stat.islnk is not defined'

script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumFileExists(script).count()
print('Number of file checks: ', count)

>>> Number of file checks: 1
```