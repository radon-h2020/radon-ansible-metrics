# Number of ```uri```

The [```uri``` module](https://docs.ansible.com/ansible/2.3/uri_module.html) allows interations with HTTP and HTTPS web services and supports Digest, Basic and WSSE HTTP authentication mechanisms.
To this end it requires to specify an ```url```.

This property counts the occurrences of ```uri``` modules.

---


## Example
The following example has **one** parameters.

``` yaml
- name: Check that you can connect (GET) to a page and it returns a status 200
  uri:
    url: http://www.example.com
```

---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```uri``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_uri import NumUri

str = '- name: Check that you can connect (GET) to a page and it returns a status 200\n\turi:\n\t\turl: http://www.example.com'

script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumUri(script).count()
print('Number of uri: ', count)

>>> Number of uri: 1
```