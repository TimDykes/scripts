#!/bin/bash

##./plot_tP.py ${1}/cube.00001 "Temperature vs Radial Distance" "Pressure vs Radial Distance"
./plot_i.py ${1} ${2} "Ray Intensity vs Radial Distance (showing ${2} rank(s) of ${3})"
./plot_tau.py ${1} ${2} "Optical Depth vs Radial Distance (showing ${2} rank(s) of ${3})"
./plot_uDot.py  ${1} ${2} "Particle uDot vs Radial Distance (showing ${2} rank(s) of ${3})"
## Single ray
./plot_i.py ${1} 1 "Ray Intensity vs Radial Distance (single ray)" 1
./plot_tau.py ${1} 1 "Optical Depth vs Radial Distance (single ray)" 1
