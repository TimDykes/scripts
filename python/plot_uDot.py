#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import csv, sys

# Read tab delimited file to array (1 line per element)
def readfile(fn, arr):
        with open(fn) as tsv:
            for line in csv.reader(tsv, delimiter='\t'):
                arr.append(line)

narg = len(sys.argv)
if narg !=  4:
    print('Error; Usage: ./plot_uDot.py filepath nfiles plottitle')

vals = []

for i in range(int(sys.argv[2])):
    # Read file
    name = sys.argv[1]+"/sruDots"+str(i)+".log"
    file = []
    readfile(name, file)

    # Convert to float
    for e in file:
        e.pop()
        if(len(e) == 4):
            vals.append(list(map(float, e)))

# Get title
title = sys.argv[3]

# Radial distance in AU
rd = [0.206265 * (np.sqrt(np.square(_[0]) + np.square(_[1]) + np.square(_[2]))) for _ in vals]

# uDots and loguDots
ud = [_[3] for _ in vals]
logud = [-10 if _ < 1e-10 else np.log10(_) for _ in ud]

plt.scatter(rd, ud, marker='.')
plt.xlabel('Radial Distance from Source (AU)')
plt.ylabel('uDot (sim internal energy unit)')
plt.title(title)
plt.savefig('uDot_vs_rd')

plt.clf()

plt.scatter(rd, logud, marker='.')
plt.xlabel('Radial Distance from Source (AU)')
plt.ylabel('log10(uDot) (sim internal energy unit)')
plt.title(title)
plt.savefig('log10uDot_vs_rd')
