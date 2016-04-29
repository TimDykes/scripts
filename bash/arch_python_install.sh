#!/bin/bash

## Roughly what I did, script untested...

## Update, install python and dependencies 
pacman -Syu
pacman -S python ipython python-pip hdf5 sqlite zeromq mercurial

## Install essentials 
pip install Cython matplotlib numpy scipy

## Extra yt dependencies
pip install sympy nose h5py

## yt 
pip install yt
