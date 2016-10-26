#!/usr/bin/python
import sys
import pickle

size = 5
if len(sys.argv) > 1:
  if sys.argv[1].isdigit():
    size = int(sys.argv.pop(1))
  elif len(sys.argv) > 2 and sys.argv[2].isdigit():
    size = int(sys.argv.pop(2))

if size > 5:
  size = 5

print "Size: " + str(size)
#the empty board
board = []

for i in range(size):
  row = []
  for j in range(size): #for each board spot
    letter = raw_input()
    row.append(letter)
  print #write a new row
  board.append(row)

if len(sys.argv) > 1:
  file = []
  file.append(board)
  pickle.dump(file, open(sys.argv[1],'w'))
else:
  print "No file!"
