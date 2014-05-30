#!/bin/bash
pip uninstall -y andrimne; python setup.py sdist bdist_wininst upload -r https://testpypi.python.org/pypi && pip install -i https://testpypi.python.org/pypi --allow-external andrimne andrimne --ignore-installed --no-deps

