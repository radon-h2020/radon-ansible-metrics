# Text entropy

It measures the entropy of the script as text.

---

## Example
The following example has entropy **4.89**.

``` yaml
---
- hosts: all
  roles:
  - common

- hosts: dbservers
  roles:
  - db
  - web
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned float``` |The entropy of the script's text  |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.text_entropy import TextEntropy

str = '---\n- hosts: all\n\troles:\n\t- common\n\n- hosts: dbservers\n\troles:\n\t- db\n\t- web' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = TextEntropy(script).count()
print('Entropy: ', count)

>>> Entropy: 4.89
```
