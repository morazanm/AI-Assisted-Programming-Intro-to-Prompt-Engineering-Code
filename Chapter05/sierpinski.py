import math
import turtle

"""
Data definitions

A point is a tuple of two numbers (x, y)
A triangle is a tuple of three points, (p1, p2, p3), for the top, left, and right vertices
"""

def drawTriangle(tringle):
    """
    Signature: triangle -> None
    Purpose: Draw the given triangle using turtle graphics
    Design idea: Draw the triangle by moving the turtle to each 
                 triangle vertex in order.
    """
    turtle.penup()
    turtle.goto(tringle[0])
    turtle.pendown()
    turtle.goto(tringle[1])
    turtle.goto(tringle[2])
    turtle.goto(tringle[0])

def midpoint(p1, p2):
    """
    Signature: point point -> point
    Purpose: Return the midpoint of the line segment connecting p1 and p2
    Design idea: The midpoint is the average of the x and y coordinates of p1 and p2.
    """
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def smallTriangle(a_triangle):
    """
    Signature: triangle -> bool
    Purpose: Determine if the given equilateral triangle is small
    Design idea: A triangle is small if the its side length is less than 10.
    """
    return math.dist(a_triangle[2], a_triangle[0]) < 10

def sierpinski(a_triangle):
    """
    Signature: Turtle triangle -> None
    Purpose: Draw the Sierpinski triangle using given triangle as the base triangle
    Design idea: If the triangle is too small, return None.
                 Otherwise, draw the given triangle and recursively draw
                 draw smaller Seerpinski triangles formed the midpoints of the sides.
    """
    if smallTriangle(a_triangle):
        return drawTriangle(a_triangle)
    else:
        midpt1 = midpoint(a_triangle[0], a_triangle[1])
        midpt2 = midpoint(a_triangle[0], a_triangle[2])
        midpt3 = midpoint(a_triangle[1], a_triangle[2])
        sierpinski((a_triangle[0], midpt1, midpt2))
        sierpinski((midpt1, a_triangle[1], midpt3))
        sierpinski((midpt2, midpt3, a_triangle[2]))
    "Termination argument: Each recursive call reduces the size of the triangle, eventually making the given triangle small and the function terminates."

def test_sierpinski():
    """
    Signature: -> None
    Purpose: Test the sierpinski function with a large triangle
    Design idea: Draw a large Sierpinski triangle and check if it is drawn correctly.
    """
    
    WIDTH = 600
    HEIGHT = math.sqrt(3/2) * (WIDTH/2) 
    p1 = (0,HEIGHT/2)
    p2 = (-WIDTH/2,-HEIGHT/2)
    p3 = (WIDTH/2, -HEIGHT/2)
    turtle.screensize(WIDTH,HEIGHT,"black")
    turtle.pencolor("hotpink")
    turtle.hideturtle()
    turtle.tracer(0)  # Disable animation for faster drawing
    sierpinski((p1,p2,p3))
    turtle.update()  # Update the screen to show the last drawn triangle
    turtle.done()

test_sierpinski()



