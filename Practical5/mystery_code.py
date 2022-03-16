# What does this piece of code do?
# Answer:draw a ramdom number between 1 and 100 if progress >=10, let progress +1 if progress < 10

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




