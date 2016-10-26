#!/usr/bin/python
import random
import sys
import pickle

#all the dice found in boggle deluxe
dice = [
['O','O','O','T','T','U'],
['D','H','H','N','O','T'],
['N','O','U','T','O','W'],
['A','A','A','S','F','R'],
['A','E','E','M','U','G'],
['A','E','N','N','M','G'],
['A','D','E','N','N','N'],
['D','D','N','R','L','O'],
['C','C','T','S','N','W'],
['F','S','I','P','R','Y'],
['A','E','E','E','E','M'],
['I','R','R','P','H','Y'],
['E','O','T','T','T','M'],
['A','A','F','I','S','R'],
['D','O','L','H','N','R'],
['C','E','S','P','T','I'],
['A','A','E','E','E','E'],
['E','I','I','I','T','T'],
['A','F','I','S','R','Y'],
['C','E','P','I','T','L'],
['E','N','S','S','S','U'],
['C','E','I','I','L','T'],
['D','H','H','O','L','R'],
['G','O','V','R','R','W'],
['K','Z','X','B','J','Qu']
]

size = 5
if len(sys.argv) > 1:
  if sys.argv[1].isdigit():
    size = int(sys.argv.pop(1))
  elif len(sys.argv) > 2 and sys.argv[2].isdigit():
    size = int(sys.argv.pop(2))

if size > 5:
  size = 5

#the empty board
board = []

numbers = [] #the order of the dice
for i in range(len(dice)): #randomize the dice order
  numbers.insert(random.randint(0, i),i)

for i in range(size):
  row = []
  for j in range(size): #for each board spot
    letter = dice[numbers[i*size+j]][random.randint(0,size)] #roll the dice
    row.append(letter) #set the letter on the board
    sys.stdout.write("%-2s" %(letter)) #write the letter padded with spaces
  print #write a new row
  board.append(row)

file = []
file.append(board)
if len(sys.argv) > 1:
  pickle.dump(file, open(sys.argv[1],'w'))
