import turtle
turtle.Screen().setup(500,500)
load_window = turtle.Screen()
turtle.speed(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white"]
my_pen = turtle.Pen()
turtle.bgcolor("black")

for x in range(360):
    my_pen.pencolor(colors[x % 8])
    my_pen.width(x/100 + 1)
    my_pen.forward(x)
    my_pen.left(59)