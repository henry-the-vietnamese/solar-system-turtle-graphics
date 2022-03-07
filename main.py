#!/usr/bin/python3

#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         25-Aug-21
# Description:  Use Turtle graphics to draw a illustration of the Solar System.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


# ------------------------------- Module Imports ------------------------------
import turtle
import drawing_functions as func


# ------------------------------- Main Function -------------------------------
def main():
    # Scale - 1 : 2,000,000,000,000 (turtle unit : centimeter)
    scale = 2000000000000

    """ Create a list of 8 planets with their elements being:
        1. name of the planet
        2. distance from each planet from the sun, measured in million km
        3. colour of the planet
        4. orbital period, measured in Earth days
    """

    planets = (
        ('Mercury', 57, 'grey', 88),
        ('Venus', 108, 'brown', 225),
        ('Earth', 149, 'cadet blue', 365),
        ('Mars', 228, 'red3', 687),
        ('Jupiter', 780, 'saddle brown', 12 * 365),
        ('Saturn', 1437, 'yellow3', 29 * 365),
        ('Uranus', 2871, 'green', 84 * 365),
        ('Neptune', 4530, 'blue', 165 * 365),
    )

    # Set up the window.
    window = turtle.Screen()
    window.title('Orbits of the Eight Planets as Circles')
    turtle.setup(width=1510, height=1010)

    # title
    text = turtle.Turtle()
    text.shape('turtle')
    text.color('black')
    func.move_turtle(text, 400, 435)
    text.write('Solar System',
               font=('Courier', 25, 'bold'), align='center')
    func.move_turtle(text, 400, 400)
    text.write('Orbits of the Eight Planets as Circles',
               font=('Courier', 22, 'bold'), align='center')

    # Scale
    # scale_border
    rectangle = turtle.Turtle()
    func.make_turtle(rectangle, 'black', 'white', 0)
    func.move_turtle(rectangle, 730, -480)
    rectangle.setheading(90)
    for _ in range(2):
        rectangle.fd(35)
        rectangle.lt(90)
        rectangle.fd(365)
        rectangle.lt(90)
    rectangle.lt(-90)
    rectangle.hideturtle()
    # scale_write_text
    func.move_turtle(text, 720, -480)
    text.write('1 : 2,000,000,000,000',
               font=('Courier', 20, 'bold'), align='right')
    text.hideturtle()

    # Sun
    sun = turtle.Turtle()
    func.make_turtle(sun, 'yellow', 'yellow', 0)
    func.move_turtle(sun, -250, -25)
    sun.begin_fill()
    sun.circle(25)
    sun.end_fill()
    sun.hideturtle()

    # 8 Orbits
    orbit = turtle.Turtle()
    func.make_turtle(orbit, 'orange', 'yellow', 2)
    x = 25              # The radius of the Sun
    size = 2

    for name, distance, colour, days in planets:
        orbit.color(colour, colour)
        orbit.pensize(size)
        distance = ((distance * 10 ** 6) * 10 ** 5) / scale
        func.move_turtle(orbit, -250, -x - distance)
        orbit.circle(x + distance)
        # Position of the orbit
        position = (days / 365) * 360
        orbit.circle(x + distance, position)
        if days == 88:
            orbit.setheading(180)
        else:
            orbit.setheading(270)
        orbit.begin_fill()
        orbit.circle(15)
        orbit.end_fill()
        orbit.setheading(0)
        func.move_turtle(orbit, -250, -x - distance)
        x += 25
        size += 1.5

    orbit.hideturtle()

    # legend_boder
    boder = turtle.Turtle()
    func.make_turtle(boder, '#F0F0F0', '#F0F0F0', 2)
    func.move_turtle(boder, 365, 300)
    boder.begin_fill()
    for _ in range(2):
        boder.fd(365)
        boder.lt(-90)
        boder.fd(610)
        boder.lt(-90)
    boder.lt(90)
    boder.end_fill()
    boder.hideturtle()

    # legends
    # title
    legend = turtle.Turtle()
    func.make_turtle(legend, 'black', 'black', 2)
    func.move_turtle(legend, 555, 250)
    legend.write('Distance to the Sun (million km)',
                 font=('Courier', 14, 'bold'), align='center')
    func.move_turtle(legend, 555, 220)
    legend.write('Orbital period (Earth days)',
                 font=('Courier', 14, 'bold'), align='center')
    # planet names
    y = 160
    for name, distance, colour, days in planets:
        func.make_turtle(legend, colour, colour, 5)
        func.move_turtle(legend, 380, y)
        legend.begin_fill()
        for i in range(4):
            legend.fd(10)
            legend.lt(-90)
        legend.end_fill()
        func.move_turtle(legend, 420, y - 15)
        legend.color('black')
        legend.write(f'{name} | {distance} | {days}', font=('Courier', 15))
        y -= 60
    legend.hideturtle()

    # Wipe the screen out.
    window.exitonclick()


# --------------------------- Call the Main Function --------------------------
if __name__ == '__main__':
    main()
