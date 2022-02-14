#!/usr/bin/python3

#
# File:         drawing_functions.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         25-Aug-21
# Description:  A list of user-defined functions that assist in drawing
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


# ------------------------------- Module Import -------------------------------
import turtle


# ---------------------------- Function Definitions ---------------------------
def make_turtle(animal, pencolour, fillcolour, size):
    animal.shape('turtle')
    animal.color(pencolour, fillcolour)
    animal.pensize(size)
    animal.speed(0)


def move_turtle(animal, x, y):
    animal.pu()
    animal.goto(x, y)
    animal.pd()
