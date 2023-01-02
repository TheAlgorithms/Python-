"""
Author Anurag Kumar | anuragkumarak95@gmail.com | git/anuragkumarak95

Simple example of fractal generation using recursion.

What is the Sierpiński Triangle?
    The Sierpiński triangle (sometimes spelled Sierpinski), also called the
Sierpiński gasket or Sierpiński sieve, is a fractal attractive fixed set with
the overall shape of an equilateral triangle, subdivided recursively into
smaller equilateral triangles. Originally constructed as a curve, this is one of
the basic examples of self-similar sets—that is, it is a mathematically
generated pattern that is reproducible at any magnification or reduction. It is
named after the Polish mathematician Wacław Sierpiński, but appeared as a
decorative pattern many centuries before the work of Sierpiński.

Requirements (pip): turtle

Usage: python sierpinski_triangle.py <int:depth_for_fractal>

Credits:
    The above description is taken from
    https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
    This code was written by editing the code from
    https://www.riannetrujillo.com/blog/python-fractal/
"""
import sys
import turtle


def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2  # find midpoint


def triangle(vertex1, vertex2, vertex3, depth):
    my_pen.up()
    my_pen.goto(vertex1[0], vertex1[1])
    my_pen.down()
    my_pen.goto(vertex2[0], vertex2[1])
    my_pen.goto(vertex3[0], vertex3[1])
    my_pen.goto(vertex1[0], vertex1[1])

    if depth > 0:
        triangle(
            vertex1, get_mid(vertex1, vertex2), get_mid(vertex1, vertex3), depth - 1
        )
        triangle(
            vertex2, get_mid(vertex1, vertex2), get_mid(vertex2, vertex3), depth - 1
        )
        triangle(
            vertex3, get_mid(vertex3, vertex2), get_mid(vertex1, vertex3), depth - 1
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError(
            "Correct format for using this script: "
            "python fractals.py <int:depth_for_fractal>"
        )
    my_pen = turtle.Turtle()
    my_pen.ht()
    my_pen.speed(5)
    my_pen.pencolor("red")

    vertices = [(-175, -125), (0, 175), (175, -125)]  # vertices of triangle
    triangle(vertices[0], vertices[1], vertices[2], int(sys.argv[1]))
