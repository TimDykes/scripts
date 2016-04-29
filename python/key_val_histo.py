import numpy as np
import matplotlib.pyplot as pl

# Get data
d0 = np.genfromtxt("/Users/tims/Code/testbed/tipsyradiate/plots/data/l3d_l2d_T_dT.dat");
d1 = np.genfromtxt("/Users/tims/Code/testbed/tipsyradiate/plots/data/l3d_l2d_z_tau1.0.dat");

# Pick two arrays
keys = d0[:,1]
vals = d0[:,2]


# Plot titles
xlab = "Radius from star (AU)"
ylab = "T (K)"
title = "Gas temperature (T)"
outfile = "average_T"

# Number of bins for histogram
nb = 50
# Number of data elements
nd = len(keys)

# For linear space
#dr = (r.max()-r.min())/50

# Init bins and create logspace bin edges
bins = [[] for i in range(nb)]
dks = np.logspace(np.log10(keys.min()), np.log10(keys.max()), nb)

# Sort values to bins based on keys
for i in range(nd):
    for j in range(len(dks)-1):
        if(keys[i]<dks[j+1]):
            id = j
            break
    bins[id].append(vals[i])

# Average bincount
av = [0] * nb
for i in range(nb):
   sum = np.sum(bins[i])
   if(sum>0):
       av[i] = sum/len(bins[i])

# Plot result
pl.plot(dks, av)
pl.title(title)
pl.xlabel(xlab)
pl.ylabel(ylab)
pl.savefig(outfile)


