#!/usr/bin/env python3


from math import pi


def circle_area(radius):
    return radius * radius * pi


def rectangle_area(side_1, side_2):
    return side_1 * side_2


def square_area(side):
    return side * side


def triangle_area(base, height):
    return 0.5 * base * height


if __name__ == '__main__':
    print(f'Area of Circle Radius 2: {circle_area(2)}')
    print(f'Area of Square with Side 2: {square_area(2)}')
    print(f'Area of Rectangle with Sides 3 and 4: {rectangle_area(3, 4)}')
