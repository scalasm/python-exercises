import turtle

def square(size):
    for side in range(4):
        turtle.fd(size)
        turtle.lt(90)

def triangle(size):
    for side in range(3):
        turtle.fd(size)
        turtle.lt(120)


def polygon(size,sides):
    angle = 360 / sides
    for side in range(sides):
        turtle.fd(size)
        turtle.lt(angle)

square(100)
turtle.color("blue")
triangle(75)
turtle.color("red")
polygon(88,10)