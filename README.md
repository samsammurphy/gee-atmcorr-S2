### Introduction

Atmospheric correction of Sentinel 2 imagery in Google Earth Engine. 

### Prerequisites

- Python
- Google Earth Engine Python API
- Jupyter Notebook
- Py6S

### Py6S

[Py6S](http://py6s.readthedocs.io/en/latest/introduction.html) is a Python interface to the 6S radiative transfer code. 6S is written in FORTRAN and used by NASA/USGS for the LEDAPS (Landsat) and MODIS surface reflectance products. 

### Installation

The easiest way to install Py6S and all dependencies (including 6S) is through the [conda](https://conda.io/docs/installation.html) package manager.

`conda config --add channels conda-forge`  
`conda install py6s`

For more information on how to install the prerequisites please see the relevant docs.

- [Py6S](http://py6s.readthedocs.io/en/latest/installation.html)
- [Google Earth Engine Python API](https://developers.google.com/earth-engine/python_install)
- [Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/install.html)
