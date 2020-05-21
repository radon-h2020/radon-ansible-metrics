# Number of suspicious comments

It measures the number of suspicious comments, i.e., those containing at least one of the following keywords: ```TODO```, ```FIXME```, ```HACK```, ```XXX```, ```CHECKME```, ```DOCME```, ```TESTME```, ```PENDING```.

---

## Example
The following example has **two** suspicious comments.


``` yaml
---
# TODO: Remove this task after Ansible 2.x npm module bug is fixed. See:
# https://github.com/ansible/ansible-modules-extras/issues/1375
- name: Ensure forever is installed (to run Node.js apps).
  npm: name=forever global=yes state=present
  become: yes
  become_user: "{{ nodejs_install_npm_user }}"
  when: nodejs_forever
# TODO: Remove this task after Ansible 2.x npm module bug is fixed. See:
# https://github.com/ansible/ansible-modules-extras/issues/1375
- name: Ensure forever is at the latest release.
  npm: name=forever global=yes state=latest
  become: yes
  become_user: "{{ nodejs_install_npm_user }}"
  when: nodejs_forever        
```
---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of suspicious comments  |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.num_suspicious_comments import NumSuspiciousComments

str = '---\n# TODO: Remove this task after Ansible 2.x npm module bug is fixed. See:\n# https://github.com/ansible/ansible-modules-extras/issues/1375\n- name: Ensure forever is installed (to run Node.js apps).\n\tnpm: name=forever global=yes state=present\n\tbecome: yes\n\tbecome_user: "{{ nodejs_install_npm_user }}"\n\twhen: nodejs_forever\n# TODO: Remove this task after Ansible 2.x npm module bug is fixed. See:\n# https://github.com/ansible/ansible-modules-extras/issues/1375\n- name: Ensure forever is at the latest release.\n\tnpm: name=forever global=yes state=latest\n\tbecome: yes\n\tbecome_user: "{{ nodejs_install_npm_user }}"\n\twhen: nodejs_forever\t' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumSuspiciousComments(script).count()
print('Number of suspicious comments: ', count)

>>> Number of suspicious comments: 2
```