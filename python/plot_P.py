#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import csv, sys
import yt

narg = len(sys.argv)

# Read tipsy file
if narg > 1:
    ds = yt.load(sys.argv[1], n_ref=8)
else:
    print('Error! Must pass at minimum intensity input filename')

if(narg > 2):
	title = sys.argv[2]
else:
	title = ''

# Get temperature, coordinates, radial distance and log temperature
dd = ds.all_data()
t = dd['Gas','Temperature'][:]
d = dd['Gas','Density'][:]

# Convert density to cgs
kpcUnit = 1e-9
solUnit = 0.23262
lenUnit = kpcUnit * 3.086e+21
massUnit = solUnit * 1.9891e+33
densUnit = massUnit / lenUnit**3

d = densUnit * d

# Pressure = rho * kB/mu/mp * T
# Mean mol weight from gasoline params
mu = 1.2195121951219512
# Boltzemann constant / mass hydrogen
kB_mp = 8.2506188037e7

P = d * (kB_mp / mu) * t
logP = np.log10(P)

# Radial distance in AU
rd = 0.206265 * np.sqrt(np.square(dd['Gas','Coordinates'][:,0].v) + np.square(dd['Gas','Coordinates'][:,1].v) + np.square(dd['Gas','Coordinates'][:,2].v))

# Do pressure
plt.scatter(rd, P, marker='.')
plt.xlabel('Radial Distance from Source (AU)')
plt.ylabel('Pressure (P = rho * kB/mp/mu * T) (CGS)')
plt.title(title)
plt.savefig('P_vs_rd')

plt.clf()

# Do 
plt.scatter(rd, logP, marker='.')
plt.xlabel('Radial Distance from Source (AU)')
plt.ylabel('log10(Pressure) (P = rho * kB/mp/mu * T) (CGS)')
plt.title(title)
plt.savefig('logP_vs_rd')

