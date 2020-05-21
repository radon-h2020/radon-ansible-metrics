# Blocks error handling

It measures the number of times [errors are handled within the blocks](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html) in its tasks.

Blocks introduce the ability to handle errors in a way similar to exceptions in most programming languages.
The tasks in the block would execute normally, if there is any error the rescue section would get executed with whatever you need to do to recover from the previous error. The always section runs no matter what previous error did or did not occur in the block and rescue sections.

---

## Example
The following example has 1 block error handling.

``` yaml
- name: Attempt and graceful roll back demo
  block:          # This block handle errors with rescue and always
    - debug:
        msg: 'I execute normally'
    - name: i force a failure
      command: /bin/false
    - debug:
        msg: 'I never execute, due to the above task failing, :-('
  rescue:
    - debug:
        msg: 'I caught an error'
    - name: i force a failure in middle of recovery! >:-)
      command: /bin/false
    - debug:
        msg: 'I also never execute :-('
  always:
    - debug:
        msg: "This always executes"

- name: A task with a block that does not handle errors
  block:        # This block does not
    - debug:
        msg: 'I execute normally'
    - name: i force a failure
      command: /bin/false
    - debug:
        msg: 'I never execute, due to the above task failing, :-('
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of blocks error handling |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_blocks_error_handling import NumBlocksErrorHandling

str = '- name: Attempt and graceful roll back demo\n\tblock:\t\t\t\t\t# This block handle errors with rescue and always\n\t\t- debug:\n\t\t\t\tmsg: \'I execute normally\'\n\t\t- name: i force a failure\n\t\t\tcommand: /bin/false\n\t\t- debug:\n\t\t\t\tmsg: \'I never execute, due to the above task failing, :-(\'\n\trescue:\n\t\t- debug:\n\t\t\t\tmsg: \'I caught an error\'\n\t\t- name: i force a failure in middle of recovery! >:-)\n\t\t\tcommand: /bin/false\n\t\t- debug:\n\t\t\t\tmsg: \'I also never execute :-(\'\n\talways:\n\t\t- debug:\n\t\t\t\tmsg: "This always executes"\n\n- name: A task with a block that does not handle errors\n\tblock:\t\t\t\t# This block does not\n\t\t- debug:\n\t\t\t\tmsg: \'I execute normally\'\n\t\t- name: i force a failure\n\t\t\tcommand: /bin/false\n\t\t- debug:\n\t\t\t\tmsg: \'I never execute, due to the above task failing, :-(\'' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumBlocksErrorHandling(script).count()
print('Number of blocks with rescue/always: ', count)

>>> Number of blocks with rescue/always: 1
```