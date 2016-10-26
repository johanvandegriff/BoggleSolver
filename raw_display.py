#!/usr/bin/python
import sys
import pickle

if len(sys.argv) == 1:
  quit()

file = pickle.load(open(sys.argv[1],'r')) #import the board

for item in file:
  print item
  print
