# Number of interactions with user

It measures the number of interactions with users by means of the module [```prompts```](https://docs.ansible.com/ansible/2.5/user_guide/playbooks_prompts.html) in the script.

---

## Example
The following example from the [Ansible's documentation](https://docs.ansible.com/ansible/2.5/user_guide/playbooks_prompts.html) repository has **three** ```prompts```:

``` yaml
- hosts: all
  remote_user: root

  vars_prompt:
    - name: "name"
      prompt: "what is your name?"
    - name: "quest"
      prompt: "what is your quest?"
    - name: "favcolor"
      prompt: "what is your favorite color?"
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```prompt``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_user_initeraction import NumUserInteraction

str = '- hosts: all\n\tremote_user: root\n\n\tvars_prompt:\n\t\t- name: "name"\n\t\t\tprompt: "what is your name?"\n\t\t- name: "quest"\n\t\t\tprompt: "what is your quest?"\n\t\t- name: "favcolor"\n\t\t\tprompt: "what is your favorite color?"' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumUserInteraction(script).count()
print('Number of user interaction: ', count)

>>> Number of user interaction: 3
```