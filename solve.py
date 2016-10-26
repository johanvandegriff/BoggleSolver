#!/usr/bin/python
import sys
import re  #this is the regular expression library
import pickle

#import the board
if len(sys.argv) == 1:
  quit()

file = pickle.load(open(sys.argv[1],'r'))
board = file[0]
size = len(board)

minwordlength = 4
if len(sys.argv) > 2 and sys.argv[2].isdigit():
  minwordlength = int(sys.argv[2])

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

for x in range(size):
  for y in range(size):
    letter = board[x][y]
    quantities[alphabet.index(letter)] += 1 #increase the quantity of the letter
    if letter in excluded: #if the letter is in excluded
      excluded.remove(letter) #remove the letter from excluded
    if letter == 'Qu' and 'U' in excluded: #if the letter is in excluded
      excluded.remove('U') #remove the letter from excluded
    for newx in range(x-1,x+2):
      for newy in range(y-1,y+2):
        if (newx>=0 and newy>=0 and newx<size and newy<size
            and not (newx == x and newy == y)):
          newletter = board[newx][newy]
          seq = letter + newletter
          if seq in excluded: #if the sequence is in excluded
            excluded.remove(seq) #remove the sequence from excluded
          if letter == 'Qu':
            seq = 'U' + newletter
          if seq in excluded: #if the sequence is in excluded
            excluded.remove(seq) #remove the sequence from excluded

#increase the number of U's by the number of Qu's
quantities[alphabet.index('U')] += quantities[alphabet.index('Qu')]

words = [] #the list of possible words

for line in open("lists/list.txt", 'r'): #sort through each word
  line = line.strip() #remove the newline
  if len(line) >= minwordlength: #if the word is long enough
    #if the word does not have too many of any letter
    if not any(line.count(alphabet[i].lower()) > quantities[i] for i in range(len(alphabet))):
      #if there are no letters not on the board in this word
      if not any(letter.lower() in line for letter in excluded):
        words.append(line); #add the word to the list of possible words

score = 0
numwords = 0
found = []
def add(word):
  found.append(word)
#  length = len(word)
#  if length < 7:
#    points = length - 3
#  elif length == 7:
#    points = 5
#  else:
#    points = 11
#  if points < 1:
#    points = 1;
#  print ("%2d" %(points)), word
#  global score
#  score += points
#  global numwords
#  numwords += 1

#import time
#x, y: the current position on the board
#word: the current word
#used: the spots the word has letters from 
def solve(x, y, word, used):
  myused = []
  for item in used: #copy used to myused
    myused.append(item)

  myused.append([x,y]); #use the current spot
  myword = word + board[x][y].lower() #add on to the word

#  print myword
#  time.sleep(0.25)
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

#print "Word Count:  " + str(numwords)
#print "Total Score: " + str(score)

outfile = []
outfile.append(board)
outfile.append(found)
pickle.dump(outfile, open(sys.argv[1],'w'))
