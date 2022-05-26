#Draw.py
# import turtle
# turtle.setup(600,400,300,200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor("pink")
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40,80)
#     turtle.circle(-40,80)
# turtle.circle(40,80/2)
# turtle.fd(40)
# turtle.circle(16,180)
# turtle.fd(40*2/3)
# turtle.done()

import turtle
def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

def snake():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("#acacac")
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)
    
if __name__ == '__main__':
    snake()