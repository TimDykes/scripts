#!/bin/bash

if [ "$#" -ne 5 ]; then
    echo "Usage: ./allplot.sh /path/to/data/ filename fileid rankstoshow totalranks"
    exit 1
fi

./plot_tP.py ${1} ${2} ${3} "Temperature vs Radial Distance" "Pressure vs Radial Distance"
./plot_i.py ${1} ${4} "Ray Intensity vs Radial Distance (showing ${4} rank(s) of ${5})"
./plot_tau.py ${1} ${4} "Optical Depth vs Radial Distance (showing ${4} rank(s) of ${5})"
./plot_uDot.py  ${1} ${4} "Particle uDot vs Radial Distance (showing ${4} rank(s) of ${5})"
## Single ray
./plot_i.py ${1} 1 "Ray Intensity vs Radial Distance (single ray)" 1
./plot_tau.py ${1} 1 "Optical Depth vs Radial Distance (single ray)" 1
