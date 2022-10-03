# simple python program

import math

# function

def parameter(a, b, c):
    return a+b+c

def semi_parameter(a, b, c):
    return (a+b+c)/2

def area(a,b,c):
    s = semi_parameter(a,b,c)
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5

def area_math(a,b,c):
    s = semi_parameter(a,b,c)
    before = (s*(s-a)*(s-b)*(s-c))
    return math.sqrt(before)


print("Give 3 sides of a triangle!")
a = (float(input("a: ")))
b = (float(input("b: ")))
c = (float(input("c: ")))
print("Parameter of the triangle: ", parameter(a,b,c))
print("Semi-parameter of the triangle: ", semi_parameter(a,b,c))
print("Area of the triangle: ", area(a,b,c))
print("Area of the triangle (using math): ", area(a,b,c))
