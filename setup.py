#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='ansiblemetrics',
      version='0.1',
      description='A module to measure metrics on Ansible scripts',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Stefano Dalla Palma',
      maintainer='Stefano Dalla Palma',
      author_email='stefano.dallapalma0@gmail.com',
      url='https://github.com/radon-h2020/radon-ansible-metrics',
      download_url='https://github.com/radon-h2020/radon-ansible-metrics/archive/0.0.1.tar.gz',
      packages=find_packages(exclude=('test',)),
      entry_points = {
        'console_scripts': ['ansible-metrics=ansiblemetrics.command_line:main'],
      },
      classifiers=[
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers",
         "Programming Language :: Python :: 3.6",
         "License :: Apache 2",
         "Operating System :: Linux"
      ],
      insall_requires=[
        'PyYAML',
        'python-interface,
        'statistics',
        'parameterized',
        'pytest'
      ]
)
