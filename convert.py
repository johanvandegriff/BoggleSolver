#!/usr/bin/python
import sys
import pickle

if len(sys.argv) == 1:
  quit()

board = pickle.load(open(sys.argv[1],'r')) #import the board

file = []
file.append(board)

pickle.dump(file, open(sys.argv[1],'w')) #write the board
