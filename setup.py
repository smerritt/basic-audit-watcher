#!/usr/bin/env python
from setuptools import setup

setup(name='basic_audit_watcher',
      version='0.0.1',
      packages=['basic_audit_watcher'],
      entry_points={
          'swift.object_audit_watcher': [
              'basic = basic_audit_watcher:Watcher']})
