#cases in 2022.3.7
a = 19245301
#cases in 2021.3.7
b = 4218520
#cases in 2020.3.7
c = 271
#difference between 2021 and 2020
d = b-c
#difference between 2022 and 2021
e = a-b
#comparation between d and e
print(d>e)
#It is false, so e is bigger.2022 has the greatest number of new COVID-19 cases

#Booleans

X=bool("1")
Y=bool("2")
W=X and Y
print("W =",W)

X=bool(520)
Y=bool(250)
W=X and Y
print("W =",W)

X=bool("A")
Y=bool("B")
W=X and Y
print("W =",W)

X=bool(0)
Y=bool(1)
W=X and Y
print("W =",W)

X=bool(1)
Y=bool(0)
W=X and Y
print("W =",W)

X=bool("A")
Y=bool(" ")
W=X and Y
print("W =",W)

X=bool("")
Y=bool("A")
W=X and Y
print("W =",W)
