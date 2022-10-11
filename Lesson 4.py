from cmath import sqrt
from itertools import product
import math
#Software to solve for sides of Right Angle Triangle (Using Pythagora's theorem)

#Functions
def calc_hypotenus(x, y) : #x - opp, y - adj
    return math.sqrt((int(x)*int(x))+(int(y) * int (y))) #- sqrt (opp^2 + adj^2)


def calc_opposite(x, y) : #x - hyp, y - adj
    return math.sqrt((int(x)* int(x))-(int(y)* int(y))) #- sqrt (hyp^2 - adj^2)


def calc_adjacent(x, y) : #x - hyp, y - opp
     return math.sqrt((int(x)* int(x))-(int(y)* int(y))) #- sqrt (hyp^2 - opp^2)

print("Enter values for all sides. (0 for missing value)") 

hyp = input("Enter hypotenus: ")
opp = input("Enter Opposite: ")
adj = input("Enter Adjacent: ")


#IF statement
output = 0 #final result
if int(hyp) == 0 :
    output = calc_hypotenus(opp, adj)
    print("The hypotenuse is ", output)

if int(opp) == 0 :
    output = calc_opposite(hyp, adj)
    print("The opposite is ", output)

if int(adj) == 0 :
    output = calc_adjacent(hyp, opp)
    print("The adjacent is ", output)

    #if all values are given
if int(hyp)!= 0 : 
        print("All values were input. Try again, and input 0 for the missing side")

if int(opp)!= 0 : 
        print("All values were input. Try again, and input 0 for the missing side")

if int(adj)!= 0 : 
        print("All values were input. Try again, and input 0 for the missing side")

    

choice = input("pick a number 1-10! : ")
choice = 5
prizes = ["iphone" , "boots" , "gift card" , "water" , "socks" , "laptop" , 
"100 bucks" , "car" , "trash" , "dog"]

print("Congrats! You won: ",prizes[int(choice)-1])





    

