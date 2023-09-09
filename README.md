# pysec2023 intro

## Setup Python

### Install
For windows you can download python from [Official Site](https://www.python.org/)

or on Linux OS by using package manager

```
apt install python3.11 python3.11-venv
```

### Create and activate virtual environment
Use `venv` module to create virtual environment (folder) with name `venv3.11`

```
python3.11 -m venv venv3.11
```

Active the environment on Linux with
```
. venv3.11/bin/activate
```
or
```
source venv3.11/bin/activate
```

On Activate the environment on Windows with
```
venv3.11\Scripts\activate
```

## Use of Package manager
Python comes with its own package manager pip which can install packages from various sources. The default source is [PyPi official repository](https://pypi.org/) 

### Install a library
While inside the virtual environment
```
pip install google
```

Check what is installed
```
pip freeze
```

Create `requirements.txt` file to maintain a list of dependencies
```
pip freeze > requirements.txt
```
