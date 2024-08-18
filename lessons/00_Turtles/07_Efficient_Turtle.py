
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle   
                     # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):

    angle = 360/sides # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        tina.forward(i/2)                              # Move tina forward by the forward distance
        tina.left(i)                              # Turn tina left by the left turn

for i in range(100):
    i= i+1
    draw_polygon(i*i)
                      # Draw a square
tina.done()
# ...                                      # Move tina to another spot on the screen

# draw_polygon(...)                        # Draw a pentagon

# ...                                      # Move tina to another spot on the screen

# draw_polygon(...)                        # Draw a hexagon


# turtle.exitonclick()                     # Close the window when we click on it
