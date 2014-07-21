#!/bin/bash -l
#
# Short slurm batch script to test two seperate builds of CUDA-Splotch with varing image sizes
# Sizes: 128sq - 2048sq
#
# Demonstration is comparing two builds of splotch, with and without use of atomics
# Usage on Piz-Daint at CSCS
# Tim Dykes
#
#SBATCH --nodes=1
#SBATCH --partition=viz
#SBATCH --time=01:00:00

# Set executables and lognames to compare
EXE1=./Splotch6-NOATOMICS
LOG1=ATOMIC
EXE2=./Splotch6-ATOMICS
LOG2=NOATOMIC

# Parameter being modifed
MODPAR=xres

# Source parameter file (should not have $MODPAR set)
PARFILE=demo_orig.par

# Log directory (this must already exist)
LOGDIR=logs

module load cudatoolkit

#-------------------------------------------------------------------
echo "Beginning image size test: CUDA atomics vs selective update"

# Loop for each image size
for ARG in 128 256 512 1024 2048
do 

# Set up scratch parameter file for test
echo "Test: ${ARG}sq"
cat $PARFILE > scratch.par
echo "$MODPAR=$ARG" >> scratch.par

# Run test one
LOGNAME=NOATOMIC_${ARG}.log
echo "$EXE1 : $MODPAR=$ARG" >> $LOGDIR/$LOGNAME
aprun -n 1 $EXE1 scratch.par >> $LOGDIR/$LOGNAME

# Run test two
LOGNAME=ATOMIC_${ARG}.log
echo "$EXE2 : $MODPAR=$$ARG" >> $LOGDIR/$LOGNAME
aprun -n 1 $EXE2 scratch.par >> $LOGDIR/$LOGNAME

done
