#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      buste
#
# Created:     26/05/2022
# Copyright:   (c) buste 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

colors = ['#C7980A', '#F4651F', '#82D8A7', '#CC3A05', '#575E76',
'#156943', '#0BD055', '#ACD338', '#4D8F06', '#A68EBD', '#5A0085', '#FFFACD',
'#FF69B4', '#B22222', '#FF7F50', '#F0F8FF', '#0000FF', '#808080', '#008000',
'#800080']

c=turtle.Turtle()
c.getscreen().bgcolor("black")
c.shape("turtle")
c.speed(300)
c.pensize(15)

while True:

    for i in range(420):
        c.pendown()
        c.circle(5)
        c.forward(8+i/16)
        c.left(30-i/10)
        c.color(colors[i%19-1])
        c.penup()



    c.setpos(200,200)

    for i in range(350):
        c.pendown()
        c.circle(10)
        c.forward(8+i/16)
        c.left(30-i/10)
        c.color(colors[i%19-2])
        c.penup()

    c.setpos(-200,200)

    for i in range(320):
        c.pendown()
        c.circle(10)
        c.forward(8+i/16)
        c.left(30-i/10)
        c.color(colors[i%19-3])
        c.penup()

    c.setpos(-200,-200)

    for i in range(200):
        c.pendown()
        c.circle(7)
        c.forward(8+i/16)
        c.left(30-i/10)
        c.color(colors[i%19-4])
        c.penup()

    c.setpos(200,-200)

    for i in range(400):
        c.pendown()
        c.circle(2)
        c.forward(8+i/16)
        c.left(30-i/10)
        c.color(colors[i%19-5])







