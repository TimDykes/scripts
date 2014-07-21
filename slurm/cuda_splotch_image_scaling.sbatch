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

# Set executables to compare
EXE1=./Splotch6-NOATOMICS
EXE2=./Splotch6-ATOMICS
# Source parameter file (should not have xres or yres set)
PARFILE=demo_orig.par
# Log directory (this must already exist)
LOGDIR=logs
# Parameter being modifed and starting value
MODPAR=xres
MODVAL=128

module load cudatoolkit

#-------------------------------------------------------------------
echo "Beginning image size test: CUDA atomics vs selective update"
echo "Test 1: 128sq"

cat PARFILE > scratch.par
echo "$MODPAR=$MODVAL" >> scratch.par

LOGNAME=NOATOMIC_128.log
echo "$EXE1 : $MODPAR=$MODVAL" >> $LOGDIR/$LOGNAME
aprun -n 1 EXE1 scratch.par >> $LOGDIR/$LOGNAME
LOGNAME=ATOMIC_128.log
echo "$EXE2 : $MODPAR=$MODVAL" >> $LOGDIR/$LOGNAME
aprun -n 1 EXE2 scratch.par >> $LOGDIR/$LOGNAME

#-------------------------------------------------------------------
echo "Test 2: 256sq"
MODVAL=256
cat PARFILE > scratch.par
echo "$MODPAR=$MODVAL" >> scratch.par

LOGNAME=NOATOMIC_256.log
echo "$EXE1 : $MODPAR=$MODVAL" >> $LOGDIR/$LOGNAME
aprun -n 1 EXE1 scratch.par >> $LOGDIR/$LOGNAME

LOGNAME=ATOMIC_256.log
echo "$EXE2 : $MODPAR=$MODVAL" >> $LOGDIR/$LOGNAME
aprun -n 1 EXE2 scratch.par >> $LOGDIR/$LOGNAME

#-------------------------------------------------------------------
echo "Test 3: 512sq"
MODVAL=512
cat PARFILE > scratch.par
echo "$MODPAR=$MODVAL" >> scratch.par

LOGNAME=NOATOMIC_512.log
echo "$EXE1 : $MODPAR=$MODVAL" >> $LOGDIR/$LOGNAME
aprun -n 1 EXE1 scratch.par >> $LOGDIR/$LOGNAME

LOGNAME=ATOMIC_512.log
echo "$EXE2 : $MODPAR=$MODVAL" >> $LOGDIR/$LOGNAME
aprun -n 1 EXE2 scratch.par >> $LOGDIR/$LOGNAME

#-------------------------------------------------------------------
echo "Test 4: 1024sq"
MODVAL=1024
cat PARFILE > scratch.par
echo "$MODPAR=$MODVAL" >> scratch.par

LOGNAME=NOATOMIC_1024.log
echo "$EXE1 : $MODPAR=$MODVAL" >> $LOGDIR/$LOGNAME
aprun -n 1 EXE1 scratch.par >> $LOGDIR/$LOGNAME

LOGNAME=ATOMIC_1024.log
echo "$EXE2 : $MODPAR=$MODVAL" >> $LOGDIR/$LOGNAME
aprun -n 1 EXE2 scratch.par >> $LOGDIR/$LOGNAME

#-------------------------------------------------------------------
echo "Test 5: 2048sq"
MODVAL=2048
cat PARFILE > scratch.par
echo "$MODPAR=$MODVAL" >> scratch.par

LOGNAME=NOATOMIC_2048.log
echo "$EXE1 : $MODPAR=$MODVAL" >> $LOGDIR/$LOGNAME
aprun -n 1 EXE1 scratch.par >> $LOGDIR/$LOGNAME

LOGNAME=ATOMIC_2048.log
echo "$EXE2 : $MODPAR=$MODVAL" >> $LOGDIR/$LOGNAME
aprun -n 1 EXE2 scratch.par >> $LOGDIR/$LOGNAME
