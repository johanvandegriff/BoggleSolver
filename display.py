#!/usr/bin/python
import sys
import pickle

if len(sys.argv) == 1:
  quit()

file = pickle.load(open(sys.argv[1],'r')) #import the board
board = file[0]

size = len(board)

score = 0;
numwords = 0
if(len(file) > 1):
  words = file[1]
  for word in words:
    length = len(word)
    if length < 7:
      points = length - 3
    elif length == 7:
      points = 5
    else:
      points = 11
    if points < 1:
      points = 1;
    print ("%2d" %(points)), word
    score += points
    numwords += 1
  print "Word Count:  " + str(numwords)
  print "Total Score: " + str(score)

for x in range(size):
  for y in range(size): #for each board spot
    sys.stdout.write("%-2s" %(board[x][y])) #write the letter padded with spaces
  print #write a new row
