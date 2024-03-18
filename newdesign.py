import turtle
import colorsys
turtle.bgcolor("brown")
turtle.tracer(100)
turtle.pensize(2)
turtle.shape("square")
turtle.write("merry christmas")
h = 0.5
for i in range(250):
    col = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.01
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.fd(i)
    turtle.lt(100)
    turtle.circle(30)
    for j in range(2):
        turtle.fd(i*j)
        turtle.rt(109)
    turtle.end_fill()
turtle.done()
