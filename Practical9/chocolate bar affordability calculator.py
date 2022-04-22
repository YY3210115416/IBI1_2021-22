#I use money=100, price=6 as example.
import math
money=100
price=6
def chocolate_calculate(money):
    chocolate_bar=math.floor(money/price)
    change=money%price
    print(chocolate_bar,change)
    return chocolate_bar,change
chocolate_calculate(money)
    