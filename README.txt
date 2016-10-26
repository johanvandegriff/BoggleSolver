This collection of programs creates and solves Boggle boards.

create.py - Creates a boggle board.
usage: ./create.py
       ./create.py FILE
       ./create.py SIZE
       ./create.py FILE SIZE
       ./create.py SIZE FILE
default size = 5

solve.py - Solves a boggle board created by create.py.
(Does not display the solutions.)
usage: ./solve.py FILE [MIN WORD LENGTH]
default min word length = 4

display.py - Displays a board and the solutions, if any.
usage: ./display.py FILE

input.py - Writes the user input to a boggle board file.
usage: ./input.py FILE

boards/ - A directory of 1000 solved boards.

convert.py - Converts the old format of the board to the new one.

deconvert.py - Converts the new format of the board to the old one.

lists/ - The lists of words.

old/ - The original boggle program.

raw_display.py - Displays all the data from a board file in list form.

stats/ - Programs and documents for analyzing the 1000 boards and the board
         with 10,000 words.

What is Boggle?
From the Boggle Wikipedia page:

Boggle is a word game designed by Allan Turoff and originally distributed by
Parker Brothers. The game is played using a plastic grid of lettered dice, in
which players attempt to find words in sequences of adjacent letters.

Rules

The game begins by shaking a covered tray of 16 cubic dice, each with a
different letter printed on each of its sides. The dice settle into a 4×4 tray
so that only the top letter of each cube is visible. After they have settled
into the grid, a three-minute sand timer is started and all players
simultaneously begin the main phase of play.

Each player searches for words that can be constructed from the letters of
sequentially adjacent cubes, where "adjacent" cubes are those horizontally,
vertically, and diagonally neighboring. Words must be at least three letters
long, may include singular and plural (or other derived forms) separately, but
may not use the same letter cube more than once per word. Each player records
all the words he or she finds by writing on a private sheet of paper. After
three minutes have elapsed, all players must immediately stop writing and the
game enters the scoring phase.

In the scoring phase, each player reads off his or her list of discovered
words. If two or more players wrote the same word, it is removed from all
players' lists. Any player may challenge the validity of a word, in which case
a previously nominated dictionary is used to verify or refute it. For all words
remaining after duplicates have been eliminated, points are awarded based on
the length of the word. The winner is the player whose point total is highest,
with any ties typically broken by count of long words.

One cube is printed with "Qu." This is because Q is nearly always followed by
U in English words (see exceptions), and if there were a Q in Boggle, it would
be challenging to use if a U did not, by chance, appear next to it. For the
purposes of scoring Qu counts as two letters: squid would score two points (for
a five-letter word) despite being formed from a chain of only four cubes.

Boggle Deluxe

Big Boggle, later marketed as Boggle Master and Boggle Deluxe, featured a 5×5
tray, and disallowed 3-letter words. Some editions of the Big Boggle set
included an adapter which could convert the larger grid into a standard 4×4
Boggle grid.
