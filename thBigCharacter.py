import turtle
import time

def progressBar():
    for i in range (1, 51):
        a = "*" * i
        b = "." * (50 - i)
        print("Prgress: [{}->{}]".format(a, b))
        time.sleep(0.02)

def curses(up, down):
    turtle.penup()
    turtle.goto(up, down)
    turtle.pendown()

def theBigCharacter():
    progressBar()
    turtle.speed(30)
    turtle.pensize(30)
    turtle.pencolor('blue')
    curses(-150, 0)
    turtle.fd(300)
    curses(0, 150)
    turtle.seth(270)
    turtle.circle(-500, 45)
    curses(20, -50)
    turtle.seth(-45)
    turtle.fd(200)
    turtle.done()

if __name__ == '__main__':
    theBigCharacter()