![Build](https://github.com/radon-h2020/radon-ansible-metrics/workflows/Build/badge.svg)
![Documentation](https://github.com/radon-h2020/radon-ansible-metrics/workflows/Documentation/badge.svg)
![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/radon-h2020/radon-ansible-metrics)
![LGTM Alerts](https://img.shields.io/lgtm/alerts/github/radon-h2020/radon-ansible-metrics)
![pypi-version](https://img.shields.io/pypi/v/ansiblemetrics)
![pypi-status](https://img.shields.io/pypi/status/ansiblemetrics)
![release-date](https://img.shields.io/github/release-date/radon-h2020/radon-ansible-metrics)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![python-version](https://img.shields.io/pypi/pyversions/ansiblemetrics)


For full documentation visit the [radon-h2020.github.io](https://radon-h2020.github.io/radon-ansible-metrics/).

# AnsibleMetrics

**AnsibleMetrics** is a Python-based static source code analyzer for Ansible blueprints that helps to quantify the characteristics of infrastructure code to support DevOps engineers when maintaining and evolving it. 
It currently supports 46 source code metrics, though other metrics can be derived by combining the implemented ones.

It represents a step forward towards closing the gap for the implementation of software quality in-struments to support DevOps engineers when developing and maintaining infrastructure code and the development of measurement models for its quality!


## How to install

Installation is made simple by the [PyPI repository](https://pypi.org/project/ansiblemetrics).
Download the tool and install it with:

```pip install ansible-metrics```

or, alternatively from the source code project directory:

```
pip install -r requirements.txt
pip install .
```


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

## How to contribute

First, clone the repository as following:

```git clone https://github.com/radon-h2020/radon-ansible-metrics.git```

Then, move to the folder location and run

```pip install -r requirements.txt```

to install dependencies.

Execute ```pytest``` to run the test suite.


### **Step 1: Create a new branch to work on the metric**
Create a branch to implement (or update) and test a given metrics.

Move to project folder and run the following commands:
* ```git checkout master``` to move to branch ```master```
* ```git pull``` to be sure to be updated with the latest version
* ```git checkout -b <metric_name>``` to create and move to the new working branch.


### **Step 2: Document metric**

First, document the new metric with the intended behaviour and examples in the [docs](docs/) folder.

Name the documentation file with the metric name and follow the format present in the existing metrics to describe it.


### **Step 3: Create Test Case**

Create a test case in the [tests](tests/) folder and name it as **tests_\<metric\>_count.py**. 


### **Step 4: Implement metric**
Finally, create the script that implement the metric in the folder [ansiblemetrics/<general|playbook>](ansiblemetrics/).

Define the method to test with an empty body.

Run ```pytest``` to make sure test cases implemented at Step 3 **fail**.

Implement the body of the method.

Run ```pytest``` again to make sure test cases implemented at Step 3 **pass**.


### **Step 4: Commit your work**
Move to project folder and run the following commands:

* ```git add <modified_file>``` for each modified files, ```git add .``` to add all modified files (be carefull that the right files are added when using this option);

* ```git status``` is helpful to check what files have been changed/added/deleted;

* Once ready, run ```git commit -m "A message describing the work done"```;

* Finally, ```git push origin/<branch_name>``` and open a pull request if you desire to integrate your changes to the master branch;

<br>


## CHANGELOG
For information about the releases history see the [CHANGELOG](CHANGELOG.md)
