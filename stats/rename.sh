#!/bin/bash

for file in `ls boards`
do
  newfile=`expr "$file" + 0`
  newfile=`printf "%3s" "$newfile" | tr " " "0"`
  mv "boards/$file" "boards/$newfile"
done
