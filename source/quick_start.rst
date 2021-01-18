Quick Start
###########

Installation:

``pip install ansiblemetrics``


Python Usage
************

Run all metrics
===============

.. code-block:: python

    from ansiblemetrics.metrics_extractor import extract_all

    script = '''
    ---
    - hosts: all

      tasks:
      - name: This is a task!
        debug:
          msg: "Hello World"
    '''

    metrics = extract_all(script)

    metrics['lines_code']
    >> 5

    metrics['num_tasks']
    >> 1


Run specific metrics
====================

.. code-block:: python

   from ansiblemetrics.general.lines_code import LinesCode
   from ansiblemetrics.playbook.num_tasks import NumTasks

    script = '''
    ---
    - hosts: all

      tasks:
      - name: This is a task!
        debug:
          msg: "Hello World"
    '''

    LinesCode(script).count()
    >> 5

    NumTasks(script).count()
    >> 1



Command-Line Usage
******************

``ansible-metrics --omit-zero-metrics path/to/playbook.yml --dest path/to/report.json``

.. code-block:: RST

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