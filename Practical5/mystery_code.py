# What does this piece of code do?
# Answer:Let progress start at 0,and when it is smaller than 10,let it add 1 at a time and draw a random number, until progress=10, and then print the last random number drawn between 1 and 100.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress<10:
	progress+=1
	n = randint(1,100)

print(n)




