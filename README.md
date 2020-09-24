# UI-Automation
This repo has sample UI Test Automation code written in python.

## Steps to setup
* Clone the repository

Python modules required for execution of Regression Test Suite are

* python 3.6
* chrome web driver
* selenium
* holmium.core

### Installation :
Need to install these packages
> pip install requirements.txt

### For Running Test Cases

> nosetests -v tests\tests.py --nologcapture


File details
* tests.py, dashboard_test.py --> This file contains all test cases
  function.
* form.py --> This file contains all page source objects.
* form_pageobjects.py --> This file contains CSS selector constants.
* data_layer.py --> This file contains data used in tests and
  utility are defined here.
