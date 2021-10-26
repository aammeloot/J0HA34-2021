# Functions doing maths on circles

import math

def circumference(radius):
    c = 2*radius*math.pi
    return c

r = float(input("Enter the radius"))
print(circumference(r))

