# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 01:34:51 2020

@author: Fahim Arman
#Python 3 
#turtle
"""

import turtle

def J():
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(75)
    turtle.circle(-25,180)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    
    turtle.forward(10)
    turtle.pendown()
    
def T():  
    turtle.penup()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(180)
    turtle.pendown()
    
    turtle.forward(50)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(25)
    turtle.pendown()
    
    turtle.left(90)
    turtle.forward(100)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(25)
    
    turtle.forward(10)
    turtle.pendown()
    

def U():
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    
    turtle.left(180)
    turtle.forward(75)
    turtle.circle(25,180)
    turtle.forward(75)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    
    turtle.forward(10)
    turtle.pendown()
    
turtle.penup()
turtle.pensize(10)
turtle.speed(9)

def TJU():
    turtle.speed(0)
    turtle.penup()
    turtle.pensize(10)
    turtle.fd(-250)
    T()
    J()
    U()
    turtle.hideturtle()
    turtle.done()

if __name__ == '__main__':
    TJU()