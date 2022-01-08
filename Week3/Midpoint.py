from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper on the middle of the first row.
"""


def main():
    # Condtionals if world 1 by 1
    if front_is_blocked():
        put_beeper()

    # Condtionals if world more than 2 by 2
    coloring_street()
    while no_beepers_present():
        find_center_from_right_side()
        if no_beepers_present():
            move_to_left_side()
        if no_beepers_present():
            find_center_from_left_side()
        if no_beepers_present():
            move_to_right_side()


# If Karl didnt find solution on left side, go to right
def move_to_right_side():
    turn_right()
    move()
    while corner_color_is(ORANGE):
        move()


'''
Function remove first coloring if even streest. Next checked two next coloring beepers.
If one next beeper coloring and next beeper blank, colored one is center.
If two folowing beepers is colored, remove last beeper from left.
'''


def find_center_from_left_side():
    if corner_color_is(ORANGE):
        paint_corner(BLANK)
    turn_right()
    move()
    if corner_color_is(ORANGE):
        move()
    if corner_color_is(BLANK):
        turn_right()
        paint_corner(BLANK)
        put_beeper()
    if corner_color_is(ORANGE):
        turn_right()
        move()
        paint_corner(BLANK)
    if beepers_present():
        check_side_by_color()


def check_side_by_color():
    if front_is_clear():
        move()
    paint_corner(BLANK)


# If Karl didnt find solution on right side, go to left
def move_to_left_side():
    turn_right()
    move()
    while corner_color_is(ORANGE):
        move()


# Coloring all first street, if even first and last blank. If odd first is blank, last is colored.
def coloring_street():
    while front_is_clear():
        move()
        if front_is_clear():
            paint_corner(ORANGE)
            move()
            paint_corner(ORANGE)


'''
Function remove last coloring if odd streest. Next checked two next coloring beepers.
If one next beeper coloring and next beeper blank, colored street is center.
If two folowing beepers is colored, remove last beeper from right.
'''


def find_center_from_right_side():
    if corner_color_is(ORANGE):
        paint_corner(BLANK)
    turn_right()
    move()
    check_color()


def turn_right():
    turn_left()
    turn_left()


def check_color():
    if corner_color_is(ORANGE):
        move()
    if corner_color_is(BLANK):
        turn_180_degrees()
        move()
        paint_corner(BLANK)
        put_beeper()
    if corner_color_is(ORANGE):
        turn_180_degrees()
        move()
        paint_corner(BLANK)
    if beepers_present():
        check_side_by_color()


def turn_180_degrees():
    turn_left()
    turn_left()


if _name_ == '_main_':
    run_karel_program('Midpoint.w')