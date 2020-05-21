[![Build Status](https://travis-ci.com/radon-h2020/radon-ansible-metrics.svg?token=5ombixLKK1T1YhFSj8KX&branch=master)](https://travis-ci.com/radon-h2020/radon-ansible-metrics)



For full documentation visit the [radon-h2020.github.io](https://radon-h2020.github.io/radon-ansible-metrics/).

# AnsibleMetrics

**AnsibleMetrics** is a Python-based static source code analyzer for Ansible blueprints that helps to quantify the characteristics of infrastructure code to support DevOps engineers when maintaining and evolving it. 
It currently supports 46 source code metrics, though other metrics can be derived by combining the implemented ones.

It represents a step forward towards closing the gap for the implementation of software quality in-struments to support DevOps engineers when developing and maintaining infrastructure code and the development of measurement models for its quality!


## How to install

Installation is made simple by the PyPI repository.
Download the tool and install it with:

```pip install ansible-metrics```

or, alternatively from the source code project directory:

```
pip3 install -r requirements.txt
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