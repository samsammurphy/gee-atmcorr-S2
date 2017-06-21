### Introduction

Atmospheric correction of Sentinel 2 imagery in Google Earth Engine. 

### Installation

#### Recommended: Docker

The following [docker](https://www.docker.com/community-edition) container has all dependencies to run the code in this repository

`docker pull samsammurphy/ee-python3-jupyter-atmcorr:v1.0`

#### Alternative: Manual installation 

This repo has the following rerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [Google Earth Engine Python API](https://developers.google.com/earth-engine/python_install_manual)
- [Jupyter](http://jupyter.readthedocs.io/en/latest/install.html)
- [Py6S](http://py6s.readthedocs.io/en/latest/installation.html)

### Usage

To run the docker container with access to a web browser

`$ docker run -i -t -p 8888:8888 samsammurphy/ee-python3-jupyter-atmcorr:v1.0`

Once inside the container, authenticate Earth Engine

`# earthengine authenticate`

then grab the source code for this repo

`# git clone https://github.com/samsammurphy/gee-atmcorr-S2`

and run the example jupyter notebook

`# jupyter notebook gee-atmcorr-S2/Sentinel2_Atmcorr.ipynb --ip='*' --port=8888 --allow-root`

this will print out a URL that you can copy/paste into your web browser to run the code.
