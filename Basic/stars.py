import turtle
import math 
import random

turtle.tracer(False)
turtle.setup(1920,1200)

def colored_star(x, y, heading, size, color, alt_color, iterations):

    turtle.setheading(heading)

    if iterations <= 0:
        return
    else:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        turtle.color(color)
        turtle.width(4)
        if iterations == 5:
            turtle.pencolor("black")
        else:
            turtle.pencolor(color)
        turtle.begin_fill()

        x_sum = 0
        y_sum = 0
        count = 0

        angle = 120
        for side in range(5):
            x_sum += turtle.xcor()
            y_sum += turtle.ycor()
            count += 1
            turtle.forward(size)
            turtle.right(angle)
            turtle.forward(size)
            turtle.right(72 - angle)
        
        turtle.end_fill()

        center_x = x_sum / count
        center_y = y_sum / count

        distance = ((center_x - x)**2 + (center_y - y)**2)**0.5
        angle = math.tan((y-center_y)/(x-center_x)) * 180 / math.pi

        #print("Center coordinates:", center_x, center_y)
        #print("Angle ", angle, "Distance", distance)
        turtle.penup()
        turtle.right(180+angle)
        
        #turtle.color("black")
        turtle.fd(distance * 1/3)
        turtle.pendown()
        #color = "red" if color == "white" else "white"
        iterations -= 1
        x = turtle.xcor()
        y = turtle.ycor()
        size *= 0.7
        
        colored_star(x, y, heading, size, alt_color, color, iterations)
    

for i in range(2000):
    x = random.randint(-1000, 1000)
    y = random.randint(-1000, 1000)
    size = random.randint(20, 100)
    if i % 10 == 0:
        colored_star(x, y, 0, size*2, "red", "white", 5)
    else:
        colored_star(x, y, 0, size, "gray", "white", 5)

turtle.done()
