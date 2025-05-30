import turtle

turtle.Screen().bgcolor("yellow")

sc=turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome To Turtle Window")

board= turtle.Turtle()

length= 150
width= 100

for i in range(2):
    board.forward(length)
    board.left(90)
    board.forward(width)
    board.left(90)