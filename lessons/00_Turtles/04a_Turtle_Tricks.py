"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=700, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
tina.hideturtle()
# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()
# tina.penup()
# tina.goto(0,-200)
# for i in range(4):  
#     tina.forward(50)    
#     tina.left(90)
# tina.penup()
# tina.goto(0,-100)
# tina.pendown()
# for i in range(4):
#     tina.forward(50)
#     tina.left(90)  
# tina.penup()
# tina.goto(0,200)
# tina.pendown()
# for i in range(4):
#     tina.forward(50)
#     tina.left(90)          
# tina.penup()
# tina.goto(0,-150)
# tina.pendown()
# for i in range(4):
#     tina.forward(50)
#     tina.left(90)          
# tina.penup()
# tina.goto(36,24)

tina.speed(0)

tina.color("silver")
for i in range (4):
    for h in range (5):
        tina.circle(50,steps=4)
        tina.forward(5)
    tina.right(90)
    tina.forward(1)

tina.color("gold")
tina.penup()
tina.goto(0,200)
tina.pendown()

for i in range (4):
    for h in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)


tina.color("red")
tina.penup()
tina.goto(0,-200)
tina.pendown()

for i in range (4):
    for h in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)




tina.color("blue")
tina.penup()
tina.goto(200,0)
tina.pendown()

for i in range (4):
    for h in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)





tina.color("teal")
tina.penup()
tina.goto(-200,0)
tina.pendown()

for i in range (4):
    for h in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)





tina.color("purple")
tina.penup()
tina.goto(-200,-200)
tina.pendown()

for i in range (4):
    for h in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)





tina.color("magenta")
tina.penup()
tina.goto(200,200)
tina.pendown()

for i in range (4):
    for h in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)





tina.color("green")
tina.penup()
tina.goto(200,-200)
tina.pendown()

for i in range (4):
    for h in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)





tina.color("maroon")
tina.penup()
tina.goto(-200,200)
tina.pendown()

for i in range (4):
    for h in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)

tina.color("green")
tina.penup()
tina.goto(200,-200)
tina.pendown()

for i in range (4):
    for h in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)






































































































































































































































































































































































































































































































































































































































































































































































































































































turtle.exitonclick()