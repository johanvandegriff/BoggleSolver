#!/usr/bin/python
import sys
import pickle

if len(sys.argv) == 1:
  quit()

file = pickle.load(open(sys.argv[1],'r')) #import the file

board = file[0]

pickle.dump(board, open(sys.argv[1],'w')) #write the board
