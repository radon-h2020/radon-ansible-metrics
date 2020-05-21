# Number of paths

It counts the number of paths in the script, identified by the parameters ```path```, ```src```, ```dest```.

---


## Example
The following example contains **three** paths


``` yaml
---
- name: "Downloading {{program_var.stdout}} from Google Drive"
  synchronize:
    src: "/mnt/gdrive/plexguide/backup/{{program_var.stdout}.tar" # 1st path
    dest: "/tmp"  # 2nd path
  become: true
  become_user: 1000

- name: Remove Password
  lineinfile:
    path: "/opt/appdata/nzbget/nzbget.conf" # 3rd path
    regexp: ControlPassword=tegbzn6789
    line: 'ControlPassword='
    state: present
  when: nzbget_conf.stat.exists == False
```


---

## Parameters

|                |Type            |Description |
|----------------|----------------|-------------------|
| **Input**      | ```io.StringIO```    |An ansible playbook|
| **Output**     | ```unsigned int```   |The number of ```path```, ```src``` and ```dest``` |
| **Exception**  | ```TypeError```      |If the type of the input parameter is not io.StringIO |
|                | ```yaml.YAMLError``` |If the input file is not a valid yaml | 

---

## How to use
Below an example on how to call the metric and the expected output for the provided example:

```python
from io import StringIO
from ansiblemetrics.playbook.num_paths import NumPaths

str = '- name: "Downloading {{program_var.stdout}} from Google Drive"\n\tsynchronize:\n\t\tsrc: "/mnt/gdrive/plexguide/backup/{{program_var.stdout}.tar" # 1st path\n\t\tdest: "/tmp"\t# 2nd path\n\tbecome: true\n\tbecome_user: 1000\n\n- name: Remove Password\n\tlineinfile:\n\t\tpath: "/opt/appdata/nzbget/nzbget.conf" # 3rd path\n\t\tregexp: ControlPassword=tegbzn6789\n\t\tline: \'ControlPassword=\'\n\t\tstate: present\n\twhen: nzbget_conf.stat.exists == False' 
script = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
count = NumPaths(script).count()
print('Number of paths: ', count)

>>> Number of paths: 3
```
