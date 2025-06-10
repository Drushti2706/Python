import turtle

# Create turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle object
pen = turtle.Turtle()
pen.color("red")
pen.begin_fill()
pen.speed(2)

# Draw heart shape
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)

pen.end_fill()
pen.hideturtle()

# Keep window open
turtle.done()
