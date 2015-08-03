#!/bin/bash

sudo rm -rf ./noseapp_workspace.egg-info ./dist/
sudo python setup.py test
sudo python setup.py register sdist upload
