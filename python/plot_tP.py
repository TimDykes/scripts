#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import csv, sys
import yt

narg = len(sys.argv)


narg = len(sys.argv)
if narg !=  6:
    print('Error; Usage: ./plot_tP.py filepath filename file_id plottitletemp plottitlepressure') 

fileid = sys.argv[3]
# Get filename
fn = sys.argv[1] + '/' + sys.argv[2] + '.' + '{:0>5}'.format(fileid) 

# Read tipsy file
ds = yt.load(fn, n_ref=8)

# Get temperature and logtemp
dd = ds.all_data()
t = dd['Gas','Temperature'][:]
logt = np.log10(t)

# Gas density
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

# Pressure and log pressure
P = d * (kB_mp / mu) * t
logP = np.log10(P)

# Radial distance in AU
rd = 0.206265 * np.sqrt(np.square(dd['Gas','Coordinates'][:,0].v) + np.square(dd['Gas','Coordinates'][:,1].v) + np.square(dd['Gas','Coordinates'][:,2].v))
print('Min RD: '+str(min(rd)))

title1 = sys.argv[4]
title2 = sys.argv[5]

# Do temp
plt.scatter(rd, t, marker='.')
plt.xlabel('Radial Distance from Source (AU)')
plt.ylabel('Temperature (K)')
plt.title(title1)
plt.savefig('T_vs_rd_'+'{:0>5}'.format(fileid))

plt.clf()

# Do logtemp
plt.scatter(rd, logt, marker='.')
plt.xlabel('Radial Distance from Source (AU)')
plt.ylabel('log(Temperature) (K)')
plt.title(title1)
plt.savefig('logT_vs_rd_'+'{:0>5}'.format(fileid))

plt.clf()

# Do pressure
plt.scatter(rd, P, marker='.')
plt.xlabel('Radial Distance from Source (AU)')
plt.ylabel('Pressure (P = rho * kB/mp/mu * T) (CGS)')
plt.title(title2)
plt.savefig('P_vs_rd_'+'{:0>5}'.format(fileid))

plt.clf()

# Do logpressure
plt.scatter(rd, logP, marker='.')
plt.xlabel('Radial Distance from Source (AU)')
plt.ylabel('log10(Pressure) (P = rho * kB/mp/mu * T) (CGS)')
plt.title(title2)
plt.savefig('logP_vs_rd_'+'{:0>5}'.format(fileid))
