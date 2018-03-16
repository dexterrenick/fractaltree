#!/usr/bin/env python3
"""
fractaltree.py
A Tree displaying how factorials work
@author Dexter Renick & Harry Liddi Brown
@version 2018-02-21
"""
__author__ = "Dexter Renick"
__version__ = "2018-02-21"

import turtle
import random

def tree(branchLen,t):
    t.pensize(branchLen / 10) #Makes the branch length smaller as it progresses
    if branchLen < 40: #Changes between 2 colors
        t.color("green") #Green at the ends
    else:
        t.color("brown") #White in the beginning

    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-8,t)
        t.left(40)
        tree(branchLen-8,t)
        t.right(20)
        t.backward(branchLen)

def main():
    window = turtle.Screen()
    window.bgcolor("black")
    t = turtle.Turtle()
    t.speed(1000)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

if __name__ == "__main__":
    main()
