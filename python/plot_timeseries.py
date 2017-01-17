#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import csv, sys
import yt
import itertools


narg = len(sys.argv)
if narg <  4 or narg >  5:
    print('Error; Usage: python plot_timeseries.py filepath plottitle nfiles [optinal: filestep] { filepath includes filename up to ., then extension will be added in XXXXX format }')

# Number of years for one timestep 
timeunit = 1.5925

# Assume distance unit is already AU
# Width of radial bins in AU, maximum distance to extend bins to (from 0)
AUstep = 1
AUmax = 15

# Step between file outputs
if(narg > 4):
	filestep = sys.argv[4]
else:
	filestep = 1



means = []
meansRHO = []

for r in range(0,int(sys.argv[3]), int(filestep)):

	# Build filename 
	fn = sys.argv[1]+'{:05}'.format(r)

	# Read tipsy file
	ds = yt.load(fn, n_ref=8)

	# Get temperature and logtemp
	dd = ds.all_data()
	t = dd['Gas','Temperature'][:]
	fid = sys.argv[3]
	rho = dd['Gas','Density'][:]

	# Radial distance in AU
	rd = np.sqrt(np.square(dd['Gas','Coordinates'][:,0].v) + np.square(dd['Gas','Coordinates'][:,1].v))
#	 + np.square(dd['Gas','Coordinates'][:,2].v))

	print("Max radius: ", max(rd))

	# Pair particles with temperature
	trd = list(zip(t,rho,rd))


	binsT = []
	binsRHO = []

	# Bin based on rd
	for i in np.arange(0,AUmax,AUstep):
		binsT.append([ e[0] for e in trd if e[2] > i and e[2] < i+AUstep ])
		binsRHO.append([ e[1] for e in trd if e[2] > i and e[2] < i+AUstep ])

	# Calculate mean temperature of each bin, append to our list of means
	means.append([ np.mean(b) for b in binsT ])
	meansRHO.append([ np.mean(b) for b in binsRHO ])

# Plot temperature vs radius for zeroth and first step

ax0 = plt.subplot(111)
ax0.set_xlabel('Radius (AU)')
ax0.set_ylabel('Temperature (K)')

h0 = []
i0 = 0
xaxis = np.arange(1,AUmax+1,AUstep)
labs = ['Disk IC', '~1.6yr']

for i in range(0,int(sys.argv[3]), filestep):
	hand0, = ax0.plot(xaxis, means[i], label='~'+str(i*1.6)+' Yrs')
	h0.append(hand0)

for l0, ms0 in zip(ax0.lines, itertools.cycle('>^+*')):
    l0.set_marker(ms0)

box0 = ax0.get_position()
ax0.set_position([box0.x0, box0.y0, box0.width * 0.8, 0.8])
ax0.legend(handles=h0, loc='center left', bbox_to_anchor=(1, 0.5))
title1 = sys.argv[2]
ax0.set_title(title1)
plt.savefig('TvsRD')

plt.clf()

# Do the same for rho 

ax1 = plt.subplot(111)
ax1.set_xlabel('Radius (AU)')
ax1.set_ylabel('Rho (simunit)')
ax1.set_yscale('log')

h1 = []
i1 = 0
for i in range(0,int(sys.argv[3]), filestep):
	hand1, = ax1.plot(xaxis, meansRHO[i], label='~'+str(i*1.6)+' Yrs')
	h1.append(hand1)

for l1, ms1 in zip(ax1.lines, itertools.cycle('>^+*')):
    l1.set_marker(ms1)

box1 = ax1.get_position()
ax1.set_position([box1.x0, box1.y0, box1.width * 0.8, 0.8])
ax1.legend(handles=h1, loc='center left', bbox_to_anchor=(1, 0.5))
title1 = sys.argv[2]
ax1.set_title(title1)
plt.savefig('RHOvsRD')

plt.clf()

# Currently we have a series of times, with means of all bins per time
# Transpose the matrix such that we have a series of means, with all times for each mean

series = [ list(m) for m in zip(*means) ]

ax = plt.subplot(111)
ax.set_xlabel('Time (Years)')
ax.set_ylabel('Temperature (K)')

h = []
i = 0
for i,s in enumerate(series,1):
	time = [ (e*filestep*timeunit) for e in np.arange(len(s)) ]
	hand, = ax.plot(time, s, label=str(i*AUstep)+' AU')
	h.append(hand)

for l, ms in zip(ax.lines, itertools.cycle('>^+*')):
    l.set_marker(ms)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, 0.8])
ax.legend(handles=h, loc='center left', bbox_to_anchor=(1, 0.5))
title1 = sys.argv[2]
ax.set_title(title1)
plt.savefig('series')
