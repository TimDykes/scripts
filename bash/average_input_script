#!/bin/bash

total=0
count=0
for i in $( awk '{ print $1; }' <input );
do
total=$(echo $total + $i | bc -l)
count=$(($count + 1))
done
total=$(echo $total / $count | bc -l)
echo $total 
