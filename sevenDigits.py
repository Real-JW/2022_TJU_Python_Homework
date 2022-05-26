import turtle
import time

def drawLine(draw): 
    turtle.color('black')
    turtle.penup()
    turtle.fd(10)
    if (draw):
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)
    turtle.penup()
    turtle.fd(10)
    turtle.right(90)

def drawGray(draw): 
    turtle.color("lightGray")
    turtle.penup()
    turtle.fd(10)
    if (draw):
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)
    turtle.penup()
    turtle.fd(10)
    turtle.right(90)

def drawDigit(digit):
    if digit in [2,3,4,5,6,8,9]:#1
        drawLine(True)
    else:
        drawGray(True)
    turtle.right(5)

    if digit in [0,1,3,4,5,6,7,8,9]:#2
        drawLine(True)
    else:
        drawGray(True)     
    turtle.left(5)

    if digit in [0,2,3,5,6,8,9]:#3
        drawLine(True)
    else:
        drawGray(True)
    turtle.right(5)
    if digit in [0,2,6,8]:#4
        drawLine(True)
    else:
        drawGray(True)

    turtle.left(90)#
    
    if digit in [0,4,5,6,8,9]:#5
        drawLine(True)
    else:
        drawGray(True)
    turtle.left(5)
    if digit in [0,2,3,5,6,7,8,9]:#6
        drawLine(True)
    else:
        drawGray(True)
    turtle.right(5)
    if digit in [0,1,2,3,4,7,8,9]:#7
        drawLine(True)
    else:
        drawGray(True)
    turtle.left(185)
    turtle.penup()
    turtle.fd(20)

def run(number):
    turtle.speed(0)
    turtle.penup()
    turtle.pensize(10)
    turtle.fd(-250)
    for i in number:
        drawDigit(eval(i))
    turtle.hideturtle()
    turtle.done()

def date():
    number = run(time.strftime('%Y%m%d',time.gmtime()))
    run(number)

def sevenDigits():
    num = input("Please choose from the following functions: 1. Date 2. Number: " )
    if num == '1':
        date()
    elif num == '2':
        number = input('Please input a number: ')
        run(number)
    else:
        print('Error')
        sevenDigits()
        
if __name__ == '__main__':
    sevenDigits()
