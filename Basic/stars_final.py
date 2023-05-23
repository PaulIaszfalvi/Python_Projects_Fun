import turtle
import math

#turtle.tracer(False)

def draw_nested_stars(x, y, angle, size, color, iterations):
    """
    Draws stars with nested, smaller stars inside.
    The stars are centered at the given (x, y) coordinates.
    The stars have five points and are rotated by the given angle.
    The first star is drawn in the given color and subsequent stars
    alternate between white and the original color.
    The nesting process is repeated for the specified number of iterations.
    """
    for i in range(iterations):
        draw_star(x, y, size, color, angle)
        #size *= 0.8
        if i % 2 == 0:
            color = "black"
        else:
            color = original_color

def draw_star(x, y, size, color, angle):

    x_sum = 0
    y_sum = 0
    count = 0

    """
    Draws a star centered at the given (x, y) coordinates
    with the specified size, color, and rotation angle.
    The star has five points.
    """
    turtle.penup()
    turtle.goto(x, y)
    
    turtle.pendown()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()

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
    direction = math.tan((y-center_y)/(x-center_x)) * 180 / math.pi

    #print("Center coordinates:", center_x, center_y)
    #print("Angle ", angle, "Distance", distance)
    turtle.right(direction)
    turtle.goto(center_x, center_y)

# Example usage
x = 0
y = 0
angle = 120
size = 200
color = "red"
iterations = 5

original_color = color
draw_nested_stars(x, y, angle, size, color, iterations)
turtle.done()


