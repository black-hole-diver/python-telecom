from asyncio import tasks
from msilib import typemask
import sys
import math
# /*
# def sum(a, b):
#     print("Your sum is", a + b)

# if __name__ == "__main__":
#     a = int(sys.argv[1])
#     b = int(sys.argv[2])
#     sum(a, b)
# */

x = 35e3
y = 12E4
z = -87.7e100

print(float(x))
print(float(y))
print(float(z))

print(round(3.4))
print(math.floor(3.8))

# strings

print('apple'.upper())
print("LO" in "Hello".upper())

# list

players = [12, 31, 27, '48', 54]
print(players)

print(players[0])
players.append(89)

print(len(players))

print(players[2:])

# tuple

players = (12, 31, 27, '48', 54)

# set
mylist = [8, 3, 2, 3, 2, 4, 5, 8, 2]
myset = set(mylist)
print(myset)

# dictionary
team = {
    91: "Ayers, Robert",
    13: "Bechham",
    1: "Contrana"}

len(team)

team[13]
print(team[13])
team[3] = "Chirazon"

print(team.values)

# branching
if 100 not in team:
    print("YES")

# loop

mylist = [3, 65, 2, 77, 9 , 33]
for i in mylist:
    print('Element: ', i)

# function

#!/usr/bin/env python

def exponents(x):
    return x**2, x**3, x**4

print(exponents(2))

# lambda functions
x = lambda a : a + 10
print(x(5))

tasks
# write a function that tells us if the given input is a leap-year or not
# read the year from a file

while(True):
    input_year = int(input("Enter the Year to be checked: "))
    if (( input_year%400 == 0)or (( input_year%4 == 0 ) and ( input_year%100 != 0))):
        print("%d is Leap Year" %input_year)
    else:
        print("%d is Not the Leap Year" %input_year)
