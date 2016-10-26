#!/usr/bin/python
import random
import sys
import re  #this is the regular expression library

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
minwordlength = 4

#the empty board
board = []

#the boggle alphabet
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Qu','R','S','T','U','V','W','X','Y','Z']

quantities = [] #the quantities of each letter

excluded = [] #which letters are not on the board
for letter in alphabet:
  excluded.append(letter) #copy the alphabet to excluded
  quantities.append(0) #fill quantities with 0's
  for letter2 in alphabet:
    excluded.append(letter + letter2)

numbers = [] #the order of the dice
for i in range(len(dice)): #randomize the dice order
  numbers.insert(random.randint(0, i),i)

for i in range(size):
  row = []
  for j in range(size): #for each board spot
    letter = dice[numbers[i*size+j]][random.randint(0,size)] #roll the dice
    row.append(letter) #set the letter on the board
    quantities[alphabet.index(letter)] += 1 #increase the quantity of the letter
    if letter in excluded: #if the letter is in excluded
      excluded.remove(letter) #remove the letter from excluded
    sys.stdout.write("%-2s" %(letter)) #write the letter padded with spaces
  print #write a new row
  board.append(row)

for x in range(size):
  for y in range(size):
    for newx in range(x-1,x+2):
      for newy in range(y-1,y+2):
        if (newx>=0 and newy>=0 and newx<size and newy<size
            and not (newx == x and newy == y)):
          seq = board[x][y] + board[newx][newy]
          if seq in excluded: #if the sequence is in excluded
            excluded.remove(seq) #remove the sequence from excluded

words = [] #the list of possible words

for line in open("../lists/list.txt", 'r'): #sort through each word
  line = line.strip() #remove the newline
  if len(line) >= minwordlength: #if the word is long enough
    #if there are no letters not on the board in this word
    if not any(letter.lower() in line for letter in excluded):
      #if the word does not have too many of any letter
      if not any(line.count(alphabet[i].lower()) > quantities[i] for i in range(len(alphabet))):
        words.append(line); #add the word to the list of possible words

print len(words)

score = 0
numwords = 0
found = []
def add(word):
  found.append(word)
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
  global score
  score += points
  global numwords
  numwords += 1


#x, y: the current position on the board
#word: the current word
#used: the spots the word has letters from 
def solve(x, y, word, used):
  myused = []
  for item in used: #copy used to myused
    myused.append(item)

  myused.append([x,y]); #use the current spot
  myword = word + board[x][y].lower() #add on to the word

  if myword in words: #if the word is in the list of possible words
    add(myword)
    words.remove(myword)
  if not any(re.search("^" + myword, word) for word in words):
    return
  for newx in range(x-1,x+2):
    for newy in range(y-1,y+2):
      if (newx>=0 and newy>=0 and newx<size and newy<size and not [newx,newy] in myused):
        solve(newx, newy, myword, myused)

for x in range(size):
  for y in range(size):
    used = []
    word = ""
    solve(x, y, word, used)

print "Words: " + str(numwords)
print "Score: " + str(score)

for i in range(size):
  for j in range(size): #for each board spot
    sys.stdout.write("%-2s" %(board[i][j])) #write the letter padded with spaces
  print #write a new row
print len(words) + numwords
