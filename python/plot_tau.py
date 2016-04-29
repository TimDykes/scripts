#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import csv, sys

# Read tab delimited file to array (1 line per element)
def readfile(fn, arr):
        print(name)
        with open(fn) as tsv:
            for line in csv.reader(tsv, delimiter='\t'):
                arr.append(line)

narg = len(sys.argv)
if (narg !=  4 and narg != 5):
    print('Error; Usage: ./plot_uDot.py filepath nfiles plottitle (optional arg: rayid)') 

vals = []
   
for i in range(int(sys.argv[2])):
    # Read file
    name = sys.argv[1]+"/tau"+str(i)+".log"
    file = []
    readfile(name, file)

    # Convert to float
    for e in file:
        e.pop()
        vals.append(list(map(float, e)))

# Get title
title = sys.argv[3]

# Get id if plotting single ray
if(narg == 5):
    id = int(sys.argv[4])
else:
    id = -1

# Do regular tau
if id >= 0:
    # Generate range in AU
    r = [float(_)*0.206265 for _ in range(len(vals[id]))]
    plt.plot(r, vals[id])
else:
    for e in vals:
        r = [float(_)*0.206265 for _ in range(len(e))]
        plt.plot(r, e)

plt.xlabel('Radial Distance from Source (AU)')
plt.ylabel(r'$\tau$')
plt.title(title)
if id >= 0:
    name = 'tau_singleray_vs_rd'
else:
    name = 'tau_vs_rd'
plt.savefig(name)

#plt.clf()

## Do log tau
#if id >= 0:
#    # Generate range in AU
#    r = [float(_)*0.206265 for _ in range(len(vals[id]))]
#    ee = [-10 if _ < 1e-10 else np.log10(_) for _ in vals[id]]
#    plt.plot(r, ee)
#else:
#    for e in vals:
#        r = [float(_)*0.206265 for _ in range(len(e))]
#        ee = [-10 if _ < 1e-10 else np.log10(_) for _ in e]
#        plt.plot(r, ee)
#
#plt.xlabel('Radial Distance from Source (AU)')
#plt.ylabel(r'$\tau$')
#plt.title(title)
#plt.savefig('logtau_vs_rd')