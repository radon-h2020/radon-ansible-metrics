<p align="center" width="100%">
    <img src="logo.png"> 
</p>


<h2 align="center">The static source code measurement tool for Ansible</h2>
<p align="center">
<a><img alt="Build Status" src="https://github.com/radon-h2020/radon-ansible-metrics/workflows/Build/badge.svg"></a>
<a><img alt="Documentation" src="https://github.com/radon-h2020/radon-ansible-metrics/workflows/Documentation/badge.svg"></a>
<a><img alt="LGTM Grade" src="https://img.shields.io/lgtm/grade/python/github/radon-h2020/radon-ansible-metrics"></a>
<a><img alt="pypi-version" src="https://img.shields.io/pypi/v/ansiblemetrics"></a>
<a><img alt="python-version" src="https://img.shields.io/pypi/pyversions/ansiblemetrics"></a>
</p>

**AnsibleMetrics** is a Python-based static source code measurement tool to characterize Infrastructure-as-Code.
It helps quantify the characteristics of infrastructure code to support DevOps engineers when maintaining and evolving it. 
It currently supports 46 source code metrics, though other metrics can be derived by combining the implemented ones.




## How to cite AnsibleMetrics

If you use AnsibleMetrics in a scientific publication, we would appreciate citations to the following paper:

```text
@article{DALLAPALMA2020100633,
    title = "AnsibleMetrics: A Python library for measuring Infrastructure-as-Code blueprints in Ansible",
    journal = "SoftwareX",
    volume = "12",
    pages = "100633",
    year = "2020",
    issn = "2352-7110",
    doi = "https://doi.org/10.1016/j.softx.2020.100633",
    url = "http://www.sciencedirect.com/science/article/pii/S2352711020303460",
    author = "Stefano {Dalla Palma} and Dario {Di Nucci} and Damian A. Tamburri",
    keywords = "Infrastructure as Code, Software metrics, Software quality",
    abstract = "Infrastructure-as-Code (IaC) has recently received increasing attention in the research community, mainly due to the paradigm shift it brings in software design, development, and operations management. However, while IaC represents an ever-increasing and widely adopted practice, concerns arise about the need for instruments that help DevOps engineers efficiently maintain, speedily evolve, and continuously improve Infrastructure-as-Code. In this paper, we present AnsibleMetrics, a Python-based static source code measurement tool to characterize Infrastructure-as-Code. Although we focus on Ansible, the most used language for IaC, our tool could be easily extended to support additional formats. AnsibleMetrics represents a step forward towards software quality support for DevOps engineers developing and maintaining infrastructure code."
}
```



## How to install

Installation is made simple by the [PyPI repository](https://pypi.org/project/ansiblemetrics).
Download the tool and install it with:

```pip install ansiblemetrics```

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
from ansiblemetrics.<general|playbook>.metric import Metric

script = 'a valid yaml script'
value = Metric(script).count()
```

where <metric> has to be replaced with the name of the desired metric module to compute the value of a specific metric. <br>
The difference between the *general* and the *playbook* modules lies in the fact that the *playbook* module contains metrics specific to playbooks (for example, the number of plays and tasks), while the *general* module contains metrics that can be generalized to other languages (for example, the lines of code).

For example, to count the number of lines of code:

```python
from ansiblemetrics.general.lines_code import LinesCode

script = """
---
- hosts: all

  tasks:
  - name: This is a task!
    debug:
      msg: "Hello World"
"""

print('Lines of executable code:', LinesCode(script).count())
```


To extract the value for the 46 metrics at once,  import the ```ansiblemetrics.metrics_extractor``` package and call the method ```extract_all()``` (in this case the return value will be a json object):

```python
from ansiblemetrics.metrics_extractor import extract_all

script = """
---
- hosts: all

  tasks:
  - name: This is a task!
    debug:
      msg: "Hello World"
"""

metrics = extract_all(script)
print('Lines of executable code:', metrics['lines_code'])
```


## CHANGELOG
For information about the releases history see the [CHANGELOG](CHANGELOG.md)
