"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=700, height=700, startx=0, starty=0)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
tina.hideturtle()
tina.pensize(1.5)
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

# tina.speed(0)

# tina.color("silver")
# for i in range (4):
#     for h in range (5):
#         tina.circle(50,steps=4)
#         tina.forward(5)
#     tina.right(90)
#     tina.forward(1)

# tina.color("gold")
# tina.penup()
# tina.goto(0,200)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)


# tina.color("red")
# tina.penup()
# tina.goto(0,-200)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)




# tina.color("blue")
# tina.penup()
# tina.goto(200,0)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)





# tina.color("teal")
# tina.penup()
# tina.goto(-200,0)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)





# tina.color("purple")
# tina.penup()
# tina.goto(-200,-200)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)





# tina.color("magenta")
# tina.penup()
# tina.goto(200,200)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)





# tina.color("green")
# tina.penup()
# tina.goto(200,-200)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)





# tina.color("maroon")
# tina.penup()
# tina.goto(-200,200)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)

# tina.color("green")
# tina.penup()
# tina.goto(200,-200)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)


# tina.color("pink")
# tina.penup()
# tina.goto(123,-123)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)



# tina.color("black")
# tina.penup()
# tina.goto(123,123)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)



# tina.color("chartreuse")
# tina.penup()
# tina.goto(-123,-123)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)



# tina.color("orange")
# tina.penup()
# tina.goto(-123,123)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)


# tina.color("navy")
# tina.penup()
# tina.goto(123,275)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)


# tina.color("cyan")
# tina.penup()
# tina.goto(-123,275)
# tina.pendown()

# for i in range (4):
#     for h in range (5):
#         tina.circle(25,steps=4)
#         tina.forward(3)
#     tina.right(90)
#     tina.forward(1)


# import turtle


# def set_turtle_image(turtle, image_name):
#     """Set the turtle's shape to a custom image."""

#     from pathlib import Path
#     image_dir = Path(__file__).parent / "images"
#     image_path = str(image_dir / image_name)

#     screen = turtle.getscreen()
#     screen.addshape(image_path)
#     turtle.shape(image_path)

# # Set up the screen
# screen = turtle.Screen()
# screen.setup(width=600, height=600)

t = turtle.Turtle()


def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

set_turtle_image(t, "moustache1.gif")
# t.color("red")
# t.circle(100)
# t.penup()
# t.goto(0,-100)
# t.pendown()
# t.circle(100)
# t.circle(100)
# t.penup()
# t.goto(0,100)
# t.pendown()
# t.circle(100)
# t.penup()
# t.goto(0,50)
# t.begin_fill()

 


def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)











def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)




screen = turtle.Screen()
screen.setup(width=600, height=600)
# screen.bgcolor('white')



def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

set_background_image(screen, "girl_blue.gif")


# This is the function that gets called when you click on the screen
def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    t.goto(x, y)
  
screen.onclick(screen_clicked) # Important! Tell Python which function to use when the screen is clicked

turtle.done()




































































































































































































































































































































































































turtle.exitonclick()