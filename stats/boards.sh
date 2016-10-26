#!/bin/sh
file=0
while true
do
  echo
  file=`printf "%10s" "$file" | tr " " "0"`
  ./create.py "boards/$file"
  ./solve.py "boards/$file"
  file=`expr "$file" "+" "1"`
done
