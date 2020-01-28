#for mathematical oppration need math library
import math
pi= math.pi
'''Creat a function foe calculating Volume of sphere'''
def Volume_of_sphere(r):
    Vol =(4/3)*pi*r*r*r
    return Vol


radius = (12)
#call the function
print('Volume of sphere :' ,Volume_of_sphere(radius))
