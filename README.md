[![Build Status](https://travis-ci.com/stefanodallapalma/ansible-metrics.svg?token=5ombixLKK1T1YhFSj8KX&branch=master)](https://travis-ci.com/stefanodallapalma/ansible-metrics)


# ansible-metrics
A python module that provides metrics for Ansible scripts.

This repository contains 50 metrics currently implemented in Python 3.6. Although, there are 5 more implicit metrics that can be derived by combining the implemented ones.
See the [documentation](https://github.com/stefanodallapalma/ansible-metrics/blob/master/docs/README.md) for further details.


## How to install and import modules locally

First, install the necessary dependencies with the command:

```pip3 install -r requirements.txt```

You can install the package locally from the project root folder with the command:

```pip3 install . ```

Once the installation succeed you can import the module in your python application with:

```python
import ansiblemetrics
```

For example, if you want to call the metric LOC, execute the following instructions:

```python
from ansiblemetrics.general.loc import LOC
from io import StringIO

metric = LOC(StringIO('key:value'))
print(metric.count())
```

The general pattern is 

```python
from ansiblemetrics.<general|playbook|tasks>.<Metric> import <Metric>
metric = <Metric>('StringIO object representing a playbook')
print(metric.count())
```

## How to use

Once installed, typing ```ansible-metrics``` will return information on usage:

```
usage: ansible-metrics [-h] [-v] file

Extract metrics from Ansible scripts. If no optional parameter is passed, the
tool computes only the general metrics which are suitable for both playbooks
and task files.

positional arguments:
  file           input file path (playbook or tasks file)

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit

 ```


## How to contribute

First, clone the repository as following:

```git clone https://github.com/stefanodallapalma/ansible-metrics.git```

Then, move to the folder location and run

```pip install configuration/requirements.txt```

to install dependencies.

Execute ```pytest``` to run the test suite.


### Step 1: Create a new branch to work on the metric
Create a branch on purpose to work on the metric implementation and testing.

Move to project folder and run the following commands:
* ```git checkout master``` to move to branch ```master```
* ```git pull``` to be sure to be updated with the latest version
* ```git checkout -b <metric_name>``` to create and move to the new working branch. The name is up to you, but it would be usefull to call it with the metric's name or acronym


### Step 2: Document metric
In [docs/README.md](https://github.com/stefanodallapalma/ansible-metrics/tree/master/docs/README.md) insert the name of the metrics and link it to its documentation in the folder [docs/playbook](https://github.com/stefanodallapalma/ansible-metrics/tree/master/docs/playbook).

Name the documentation file as the extended metric name, in uppercase with underscores (\_) in places of blank spaces. For example, if the metric is *"Number of loops"* then create the file *docs/playbook/NUMBER_OF_LOOPS.md*.

The documentation should contain at least the following elements:

* a **unique name**;
* an **acronym** (3/4 letters) to be used to identify it and to name the script implementing it;
* a **description** that explains its purpose;
* the **input** parameters;
* the **output** type;
* an **example of a playbook** for the problem at hand and the expected result of the metric wrt that playbook. The playbook of the example must be included in the test case testing the metric, along with further examples, if needed.
* an **example on how to call** the method that implement the metric. 


### Step 3: Create Test Case
* Create a test case in the tests folder and name it with *tests_<metric_acronym>_<method_to_test>.py*. For example, to test the method ```count()``` of metric "Number of loops (NLP)", the script path would results like *tests/playbook/test_nlp_count.py*.

<TODO: To insert example of test case>

### Step 4: Implement metric
Create a script in folder *ansiblemetrics/playbook/* and name it as *<metric_acronym>.py*. 

Define the method to test with an empty body.

Run ```pytest``` to make sure test cases implemented at Step 3 **fail**.

Implement the body of the function.

Run ```pytest``` again to make sure test cases implemented at Step 3 **pass**.


### Step 4: Commit your work
Move to project folder and run the following commands:
* ```git add <modified_file>``` for each modified files, ```git add .``` to add all modified files (be carefull that the right files are added whn using this option)
* ```git status``` is helpful to check what files have been changed/added/deleted.
* Once ready, run ```git commit -m "A message describing the work done"```
* Finally, ```git push origin/<branch_name>``` and open a pull request if you desire to integrate your changes to the master branch.


For further information about the implemented classes, please refer to the [wiki](https://github.com/stefanodallapalma/ansible-metrics/wiki).
