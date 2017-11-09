print('hello world')

import math
from math import floor,log10
print("How large is the radius?")
radius=int(input()) #user input of radius

def circumference(radius):
    """This code takes the user's input of radius of a circle
    and calculates the circumference of the circle"""
    return 2*radius*math.pi

print("How many significant figures?")

sig_figures=int((input()))
def round_sig(circumference, sig_figures):
                return round(circumference, (sig_figures-int(floor(log10(abs(circumference))))-1))

print("The circumference with radius:",radius,"is:",round_sig(circumference(radius),sig_figures(radius)))



"""Well these lines are a commit"""
