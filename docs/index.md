For full documentation visit [mkdocs.org](https://www.mkdocs.org).

# Welcome to the AnsibleMetrics documentation

**AnsibleMetrics** is a Python-based static source code analyzer for Ansible blueprints that helps to quantify the characteristics of infrastructure code to support DevOps engineers when maintaining and evolving it. 
It currently supports 46 source code metrics, though other metrics can be derived by combining the implemented ones.

It represents a step forward towards closing the gap for the implementation of software quality in-struments to support DevOps engineers when developing and maintaining infrastructure code and the development of measurement models for its quality!


## How to install

Installation is made simple by the PyPI repository.
Download the tool and install it with:

```pip install ansible-metrics```

or, alternatively from the source code project directory:

```
pip install -r requirements.txt
pip install .
```


## How to use

### **Command-line interface**

Run ```ansible-metrics --help``` for instructions about the usage:

```
usage: ansible-metrics [-h] [-o] [-v] src dest

Extract metrics from Ansible scripts.

positional arguments:
  src            source file (a playbook or directory of playbooks)
  dest           destination file to save results

optional arguments:
  -h, --help     shows this help message and exit
  -o, --output   shows output
  -v, --version  shows program's version number and exit
```


### **Python**


```python
from io import StringIO
from ansiblemetrics.<general|playbook>.<metric> import <Metric>

script = 'a valid yaml script'
value = <Metric>(StringIO(script).count()
```

For example, if one wants to count the number of lines of code:

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


## Metrics

AnsibleMetrics currently supports up to 46 source code metrics, implemented in Python.

Import ```ansiblemetrics.metrics_extractor``` to extract all the metrics at once (in this case the return value will be a json object):

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


Alternatively, import the ```ansiblemetrics.playbook.<metric>``` or the ```ansiblemetrics.general.<metric>``` (where \texttt{<metric>} has to be replaced with the name of the desired metric) module to compute the value of a specific metric.

The difference between the *general* and the *playbook* modules lies in the fact that the *playbook* module contains metrics specific to playbooks (for example, the number of plays and tasks), while the *general* module contains metrics that can be generalized to other languages (for example, the lines of code).

Below the list of the implemented metrics.



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
* [Number of regex](playbook/NumRegex.md)
* [Number of plays](playbook/NumPlays.md)
* [Number of roles](playbook/NumRoles.md)
* [Number of SSH](playbook/NumAuthorizedKey.md)
* [Number of tasks](playbook/NumTasks.md)
* [Number of unique names](playbook/NumUniqueNames.md)
* [Number of urls](playbook/NumUri.md)
* [Number of user interactions](playbook/NumUserInteraction.md)
* [Number of variables](playbook/NumVars.md)


<!--
## Project layout

    ansiblemetrics/
        ansible_metric.py   # Abstract class inherited by all the metrics
        ansible_modules.py  # List of modules and deprecated modules mantained by the Ansible community
        command_line.py # The comman line interface
        import_metrics.py   # List of implemented metrics
        lines_metric.py        # Abstract class inherited by all the metrics for counting lines
        metrics_extractor.py    # Main class
        utils.py    # Contains common methods 
        general/    # Contains metrics tha can be used for languages besides Ansible
        playbook/   # Metrics specific for Ansible
    docs/
        index.md  # The documentation homepage.
        general/  # The documentation of general metrics
        playbook/ # The documentation of playbook and task list metrics
-->