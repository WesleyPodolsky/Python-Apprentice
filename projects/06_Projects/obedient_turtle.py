"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from tkinter import messagebox, simpledialog, Tk
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error

t = turtle.Turtle()  
# TODO)
#   1. Create a turtle
#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
def drawSquare():
    for i in range(4):
        t.forward(10)
        t.left(90)

def drawTriangle():
    for i in range(3):
        t.forward(13)
        t.left(60)

def drawCircle():
        t.circle(8)

shape = simpledialog.askstring(title='1/3', prompt='shape?')
if shape == 'square':
     
#   3. Ask the user for the for a shape to draw
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
pass
