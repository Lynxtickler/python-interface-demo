# Python interface demo

[![CI](https://github.com/Lynxtickler/python-interface-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/Lynxtickler/python-interface-demo/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Experimental demo to force dirty interface implementation in Python

## Quickstart

Create and activate a virtual environment
```bash
$ python -m venv venv
$ source venv/bin/activate
```

Install requirements
```bash
$ pip install -r requirements.txt
```

Activate pre-commit hooks
```bash
$ pre-commit install
```

## Demo

Run interface demo
```bash
$ python interface_demo.py
```

Comment and uncomment lines as noted in the `interface_demo.py` to see the
interfaces in action, and fail the execution at various points in the program.
