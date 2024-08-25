""" Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spont on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

... # Your code here

# Change the Background Image



import random
import turtle

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

# Set up the screen
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina


turtle.shape
screen = turtle.Screen()                # Get the screen that tina is on
set_background_image(screen, "emoji2.png") # Set the background image of the screen

def set_turtle_image(turtle, image_name):
    print('skib2')

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)


def turtle_clicked(t, x, y):

    print('turtle clicked!')
    
    

tina.onclick(lambda x, y, t=tina: turtle_clicked(t, x, y))



set_turtle_image(tina, "moustache3.gif")

   
turtle.done()
