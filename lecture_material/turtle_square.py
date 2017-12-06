#!/usr/bin/python
# coding=utf-8
import turtle


def draw_square(some_name):
    for i in range(0, 4):
        some_name.forward(100)
        some_name.right(90)


def draw_diamond(some_name):
    for i in range(0, 1):
        some_name.forward(100)
        some_name.right(30)
        some_name.forward(100)
        some_name.right(150)
        some_name.forward(100)
        some_name.right(30)
        some_name.forward(100)


def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)
#    draw_square(brad)
    for i in range(0, 72):
        draw_diamond(brad)
        brad.right(5)

    window.exitonclick()


"""
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    test = turtle.Turtle()
    test.shape("circle")
    test.color("yellow")
    for t in range(0, 3):
        test.forward(100)
        test.left(120)

    """

draw_shape()
