.. ansiblemetrics documentation master file, created by
   sphinx-quickstart on Wed Dec 16 12:35:40 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the AnsibleMetrics documentation!
============================================

**AnsibleMetrics** is a Python-based static source code measurement tool to characterize Infrastructure-as-Code.
It helps quantify the characteristics of infrastructure code to support DevOps engineers when maintaining and evolving it.
It currently supports 46 source code metrics, though other metrics can be derived by combining the implemented ones.

The metrics, along with their selection rationale, are described in:

::

   @article{DALLAPALMA2020110726,
      title = "Toward a catalog of software quality metrics for infrastructure code",
      journal = "Journal of Systems and Software",
      volume = "170",
      pages = "110726",
      year = "2020",
      issn = "0164-1212",
      doi = "https://doi.org/10.1016/j.jss.2020.110726",
      url = "http://www.sciencedirect.com/science/article/pii/S0164121220301618",
      author = "Stefano {Dalla Palma} and Dario {Di Nucci} and Fabio Palomba and Damian Andrew Tamburri",
      keywords = "Infrastructure as code, Software metrics, Software quality",
      abstract = "Infrastructure-as-code (IaC) is a practice to implement continuous deployment by allowing management and provisioning of infrastructure through the definition of machine-readable files and automation around them, rather than physical hardware configuration or interactive configuration tools. On the one hand, although IaC represents an ever-increasing widely adopted practice nowadays, still little is known concerning how to best maintain, speedily evolve, and continuously improve the code behind the IaC practice in a measurable fashion. On the other hand, source code measurements are often computed and analyzed to evaluate the different quality aspects of the software developed. However, unlike general-purpose programming languages (GPLs), IaC scripts use domain-specific languages, and metrics used for GPLs may not be applicable for IaC scripts. This article proposes a catalog consisting of 46 metrics to identify IaC properties focusing on Ansible, one of the most popular IaC language to date, and shows how they can be used to analyze IaC scripts."
   }

While the tool is described in:

::

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

.. toctree::
   :maxdepth: 4
   :caption: Content

   quick_start
   apis
   license
   help

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
