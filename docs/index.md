# Welcome to the AnsibleMetrics documentation

**AnsibleMetrics** is a Python-based static source code analyzer for Ansible blueprints that helps to quantify the characteristics of infrastructure code to support DevOps engineers when maintaining and evolving it. 
It currently supports 46 source code metrics, though other metrics can be derived by combining the implemented ones.

It represents a step forward towards closing the gap for the implementation of software quality in-struments to support DevOps engineers when developing and maintaining infrastructure code and the development of measurement models for its quality!


<br>

## How to install

Installation is made simple by the PyPI repository. <br>
Download the tool and install it with ```pip install ansiblemetrics```.<br>
Alternatively, install it from the source code project directory with the following commands:

```
pip install -r requirements.txt
pip install .
```

*AnsibleMetrics* is now installed and can be used from both command-line and Python code.

<br>

## How to use

### **Command-line**

Run ```ansible-metrics --help``` for instructions about the usage:

```
usage: ansible-metrics [-h] [--omit-zero-metrics] [-d DEST] [-o] [-v] src

Extract metrics from Ansible scripts.

positional arguments:
  src                   source file (playbook or tasks file) or
                        directory

optional arguments:
  -h, --help            show this help message and exit
  --omit-zero-metrics   omit metrics with value equal 0
  -d DEST, --dest DEST  destination path to save results
  -o, --output          shows output
  -v, --version         show program's version number and exit
```

Assume that the following example is named *playbook1.yml*:

```yaml
---
- hosts: webservers
  vars:
    http_port: 80
  remote_user: root

  tasks:
  - name: ensure apache is at the latest version
    yum:
      name: httpd
      state: latest
      
- hosts: databases
  remote_user: root

  tasks:
  - name: ensure postgresql is at the latest version
    yum:
      name: postgresql
      state: latest
      
  - name: ensure that postgresql is started
    service:
      name: postgresql
      state: started
      
```

and is located within the folder *playbooks* as follows:

playbooks <br>
&nbsp;&nbsp;&nbsp;|- playbook1.yml <br>
&nbsp;&nbsp;&nbsp;|- playbook3.yml <br>
&nbsp;&nbsp;&nbsp;|- playbook3.yml <br>


Also, assume the user's working directory is the *playbooks* folder. Then, it is possible to extract source code characteristics from that blueprint by running the following command:

```ansible-metrics --omit-zero-metrics playbook1.yml --dest report.json```

For this example, the \textit{report.json} will result in 

```
{
    "filepath": "playbook1.yml",
    "avg_play_size": 10,
    "avg_task_size": 4,
    "lines_blank": 4,
    "lines_code": 20,
    "num_keys": 20,
    "num_parameters": 6,
    "num_plays": 2,
    "num_tasks": 3,
    "num_tokens": 50,
    "num_unique_names": 3,
    "num_vars": 1,
    "text_entropy": 4.37
}
```

<br>

### **Python**

*AnsibleMetrics* currently supports up to 46 source code metrics, implemented in Python. 
To extract the value for a given metric follow this pattern:

```python
from io import StringIO
from ansiblemetrics.<general|playbook>.<metric> import <Metric>

script = 'a valid yaml script'
value = <Metric>(StringIO(script).count()
```

where <metric> has to be replaced with the name of the desired metric module to compute the value of a specific metric. <br>
The difference between the *general* and the *playbook* modules lies in the fact that the *playbook* module contains metrics specific to playbooks (for example, the number of plays and tasks), while the *general* module contains metrics that can be generalized to other languages (for example, the lines of code).

For example, to count the number of lines of code:

```python
from io import StringIO
from ansiblemetrics.general.loc import LOC

script = """
---
- hosts: all

  tasks:
  - name: This is a task!
    debug:
      msg: "Hello World"
"""

metric = LOC(StringIO(script))
print('Lines of executable code:', metric.count())

# This will result in 
# > Lines of executable code: 5
```


To extract the value for the 46 metrics at once,  import the ```ansiblemetrics.metrics_extractor``` package and call the method ```extract_all()``` (in this case the return value will be a json object):

```python
from io import StringIO
from ansiblemetrics.metrics_extractor import extract_all

script = """
---
- hosts: all

  tasks:
  - name: This is a task!
    debug:
      msg: "Hello World"
"""

metrics = extract_all(StringIO(script))
print('Lines of executable code:', metrics['lines_code'])

# This will result in 
# > Lines of executable code: 5
```


<br>

Below the list of the implemented metrics and their documentation.

### General

* [Lines blank](general/LinesBlank.md)
* [Lines of code](general/LinesCode.md)
* [Lines of comment](general/LinesComment.md)
* [Number of conditions](general/NumConditions.md)
* [Number of decisions](general/NumDecisions.md)
* [Number of deprecated keywords](general/NumDeprecatedKeywords.md)
* [Number of keys](general/NumKeys.md)
* [Number of math operations](general/NumMathOperations.md)
* [Number of suspicious comments](general/NumSuspiciousComments.md)
* [Number of tokens](general/NumTokens.md)
* [Text entropy](general/TextEntropy.md)


### Playbook

* [Average play size](playbook/AvgPlaySize.md)
* [Average task size](playbook/AvgTaskSize.md)
* [Number of blocks](playbook/NumBlocks.md)
* [Number of block error handling](playbook/NumBlocksErrorHandling.md)
* [Number of commands](playbook/NumCommands.md)
* [Number of deprecated modules](playbook/NumDeprecatedModules.md)
* [Number of distinct modules](playbook/NumDistinctModules.md)
* [Number of external modules](playbook/NumExternalModules.md)
* [Number of fact modules](playbook/NumFactModules.md)
* [Number of fact modules](playbook/NumFactModules.md)
* [Number of file extists](playbook/NumFileExists.md)
* [Number of file mode](playbook/NumFileMode.md)
* [Number of file modules](playbook/NumFileModules.md)
* [Number of filters](playbook/NumFilters.md)
* [Number of ignore_error](playbook/NumIgnoreErrors.md)
* [Number of import_playbook](playbook/NumImportPlaybook.md)
* [Number of import_role](playbook/NumImportRole.md)
* [Number of import_tasks](playbook/NumImportTasks.md)
* [Number of include](playbook/NumInclude.md)
* [Number of include_role](playbook/NumIncludeRole.md)
* [Number of include_tasks](playbook/NumIncludeTasks.md)
* [Number of include_vars](playbook/NumIncludeVars.md)
* [Number of lookups](playbook/NumLookups.md)
* [Number of loops](playbook/NumLoops.md)
* [Number of name with variables](playbook/NumNameWithVars.md)
* [Number of parameters](playbook/NumParameters.md)
* [Number of paths](playbook/NumPaths.md)
* [Number of plays](playbook/NumPlays.md)
* [Number of prompts](playbook/NumPrompts.md)
* [Number of regex](playbook/NumRegex.md)
* [Number of roles](playbook/NumRoles.md)
* [Number of SSH](playbook/NumAuthorizedKey.md)
* [Number of tasks](playbook/NumTasks.md)
* [Number of unique names](playbook/NumUniqueNames.md)
* [Number of urls](playbook/NumUri.md)
* [Number of variables](playbook/NumVars.md)

