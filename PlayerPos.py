"""
Hello and welcome to EfreiZ ! Just put your function in move_player()

You will also need to define whether you want to play slow or fast. Note: the score that's really taken into account for
measuring effiency is only and only the fast method.

Infos about the rules on my GitHub : https://github.com/RousselotN/Efrei/blob/master/S1/EfreiZ/Rules


The function move_player() needs to return an ARRAY which is either [0, 1], [1, 0], [-1, 0], [0, -1] in function on where you want to move.
"""


import random

class Players:

    def __init__(self, x, y, grid, alive):
        self.x = x
        self.y = y
        self.grid = grid
        self.alive = alive

    def move_player(self):
        c = random.randint(0, 4)
        if c == 0:
            return [0, 1]
        elif c == 1:
            return [1, 0]
        elif c == 2:
            return [-1, 0]
        else:
            return [0, -1]


"""Uncomment the line you want. Fast == 1000 simulations of your code in a blink of an eye (just kidding, my gross code is slow).
Slow == basic display to sse what your algorithm is doing."""

def plays():
    return 'slow'
    # return 'fast'
