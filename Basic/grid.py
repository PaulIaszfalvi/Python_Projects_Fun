import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Grid with Coordinates")

# Set the starting position of the turtle
start_x = -250
start_y = 250

# Set the box size and gap between boxes
box_size = 50
gap = 5

# Create the turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.penup()

# Function to draw a single box with coordinates
def draw_box(x, y):
    pen.goto(x, y)
    pen.pendown()
    for _ in range(4):
        pen.forward(box_size)
        pen.right(90)
    pen.penup()

# Function to print the coordinates of a box
def print_coordinates():
    x, y = pen.pos()
    x_coord = (x - start_x) // (box_size + gap)
    y_coord = (start_y - y) // (box_size + gap)
    pen.goto(x + 15, y - 20)
    pen.write(f"({int(x_coord)}, {int(y_coord)})", align="center", font=("Arial", 8, "normal"))

# Loop to draw the grid and label each box with coordinates
for i in range(10):
    for j in range(10):
        x = start_x + (box_size + gap) * j
        y = start_y - (box_size + gap) * i
        draw_box(x, y)
        pen.goto(x + 5, y - 20)
        print_coordinates()

# Hide the turtle and display the grid
pen.hideturtle()
turtle.done()
