import turtle


def main():
    window = turtle.Screen()
    my_turtle = turtle.Turtle()
    screen = my_turtle.getscreen()
    screen.title("Meery Christmas")
    screen.bgcolor("#E731CE")

    # Drawing the tree
    my_turtle.color("green")
    my_turtle.pensize(5)
    my_turtle.begin_fill()

    # this is the right half of the tree
    my_turtle.forward(100)
    my_turtle.left(150)
    my_turtle.forward(90)
    my_turtle.right(150)
    my_turtle.forward(60)
    my_turtle.left(150)
    my_turtle.forward(60)
    my_turtle.right(150)
    my_turtle.forward(40)
    my_turtle.left(150)
    my_turtle.forward(100)

    # this is the left half of the tree
    my_turtle.left(60)
    my_turtle.forward(100)
    my_turtle.left(150)
    my_turtle.forward(40)
    my_turtle.right(150)
    my_turtle.forward(60)
    my_turtle.left(150)
    my_turtle.forward(60)
    my_turtle.right(150)
    my_turtle.forward(90)
    my_turtle.left(150)
    my_turtle.forward(133)
    my_turtle.end_fill()

    # create the trunk of the tree
    my_turtle.color("red")
    my_turtle.pensize(1)
    my_turtle.begin_fill()
    my_turtle.right(90)
    my_turtle.forward(70)
    my_turtle.right(90)
    my_turtle.forward(33)
    my_turtle.right(90)
    my_turtle.forward(70)
    my_turtle.end_fill()

    # create star at the top of tree
    my_turtle.speed(1)
    my_turtle.penup()
    my_turtle.color('yellow')
    my_turtle.goto(-28, 110)
    my_turtle.begin_fill()
    my_turtle.pendown()
    for i in range(5):
        my_turtle.forward(40)
        my_turtle.right(144)
    my_turtle.end_fill()

    # create different color balls
    def ball(trt, x, y, size=10, colour="red"):
        trt.penup()
        trt.setpos(x, y)
        trt.color(colour)
        trt.pendown()
        trt.circle(size)
        trt.end_fill()

    ball(my_turtle, 95, -5)
    ball(my_turtle, -110, -5)
    ball(my_turtle, 80, 40, size=7, colour="yellow")
    ball(my_turtle, -98,40, size=7, colour="yellow")
    ball(my_turtle, 70, 70, size=5)
    ball(my_turtle, -93, 70, size=5)