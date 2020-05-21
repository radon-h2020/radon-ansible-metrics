# Number of tokens

It measures the number of tokens in an Ansible script (separated by blank spaces).

---

## Example
The following script has **nine** tokens:

``` yaml
- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML
  include_vars:                                     
    file: username_info.yml
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of tokens  |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.general.num_tokens import NumTokens

str = '- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML\n\tinclude_vars:\n\t\tfile: username_info.yml' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumTokens(script).count()
print('Number of tokens: ', count)

>>> Number of tokens: 9
```