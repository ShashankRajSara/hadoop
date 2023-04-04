#!/bin/bash
echo "Enter a Number:"
read n
for((i=2; i<=$n/2; i++))
do
  ans=$(( n%i ))
  if [ $ans -eq 0 ]
  then
    echo "FALSE"
    exit 0
  fi
done
echo "TRUE"