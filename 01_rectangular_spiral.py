import turtle

"""
Make a rectangular spiral (see the README.md for an example)
"""

### YOUR CODE STARTS HERE
turtle.right(90)

for i in range(10, 60, 10):
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)

### YOUR CODE ENDS HERE

turtle.exitonclick()