onsset : Open Source Spatial Electrification Tool
=================================================

[![PyPI version](https://badge.fury.io/py/onsset.svg)](https://badge.fury.io/py/onsset)
[![Build Status](https://travis-ci.com/OnSSET/onsset.svg?branch=master)](https://travis-ci.com/OnSSET/onsset)
[![Coverage Status](https://coveralls.io/repos/github/OnSSET/onsset/badge.svg?branch=master)](https://coveralls.io/github/OnSSET/onsset?branch=master)
[![Documentation Status](https://readthedocs.org/projects/onsset/badge/?version=latest)](https://onsset.readthedocs.io/en/latest/?badge=latest)

# Scope

This repository contains the code version of the Open Source Spatial Electrification Tool
([OnSSET](http://www.onsset.org/)), as used for IRENA's West Africa Electrification Platform.

## Installation

### Requirements

OnSSET requires Python > 3.5 with the following packages installed:
- et-xmlfile
- jdcal
- numpy
- openpyxl
- pandas
- python-dateutil
- pytz
- six
- xlrd
- notebook
- seaborn
- matplotlib
- scipy

### Install with pip

Install onsset from the Python Packaging Index (PyPI):

```
pip install onsset
```

### Install from GitHub

Download or clone the repository and install the package in `develop`
(editable) mode:

```
git clone https://github.com/onsset/onsset.git
cd onsset
python setup.py develop
```

## Data
Input data is available for the four countries seen on the West Africa Electrification Platform
- [Burkina Faso](https://drive.google.com/drive/folders/1zmNHojgQYT_3AYmxeWQ12WwunGngtSyJ)
- [Mali](https://drive.google.com/drive/folders/1a8a35fW3jiDgdq43BK8v9qFUW1fIj56K)
- [Nigeria](https://drive.google.com/drive/folders/1N2fOnIMD_P-FsgvsJIvxj7CJDESedUIL)
- [Senegal](https://drive.google.com/drive/folders/17SaDTLyvjBm64fOs3Iai6awuvHaFBy-Z)


## Contact
For more information regarding the tool, its functionality and implementation
please visit https://www.onsset.org or contact the development team
at seap@desa.kth.se.
