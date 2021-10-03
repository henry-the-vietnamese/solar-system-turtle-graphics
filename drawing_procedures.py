#
# File:         drawing_procedures.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         25/8/2021
# Description:  Procedures assisting in drawing repetitive shapes.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

import turtle


def make_turtle(animal, pencolour, fillcolour, size):
    animal.shape('turtle')
    animal.color(pencolour, fillcolour)
    animal.pensize(size)
    animal.speed(0)


def move_turtle(animal, x, y):
    animal.pu()
    animal.goto(x, y)
    animal.pd()
