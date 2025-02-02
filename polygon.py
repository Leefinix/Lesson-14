import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400,400)

polygon = turtle.Turtle()

polygon.penup()
polygon.goto(0,100)
num_sides = int(input("Enter the number of sides: "))
side_length = 70
angle = 360.0 / num_sides
polygon.shape("circle")
polygon.pendown()

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

polygon.hideturtle()
turtle.done